#TELEGRAM : @lsahilxx
"""
Multi-Bot Orchestrator - Coordinates squad operations across 4 bots
Handles: Squad invites, match starting, squad cleanup, error recovery
"""

import asyncio
import json
import time
from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Optional

class BotState(Enum):
    """Bot operational states"""
    IDLE = "idle"
    INVITING = "inviting"
    SQUAD_READY = "squad_ready"
    IN_MATCH = "in_match"
    MATCH_ENDING = "match_ending"
    LOBBY = "lobby"
    ERROR = "error"

@dataclass
class BotInfo:
    """Information about a single bot"""
    bot_id: int
    uid: str
    state: BotState = BotState.IDLE
    in_squad: bool = False
    team_code: Optional[str] = None
    last_activity: float = 0.0
    match_count: int = 0
    error_count: int = 0

class MultiBotsOrchestrator:
    """Orchestrates operations across 4 bots"""
    
    def __init__(self, total_bots: int = 4):
        self.total_bots = total_bots
        self.squad_builder_id = 1
        self.bots: Dict[int, BotInfo] = {i: BotInfo(bot_id=i, uid="") for i in range(1, total_bots + 1)}
        self.squad_members: List[int] = []
        self.active_squad = False
        self.current_team_code = None
        self.operational_mode = "auto"  # auto or manual
        self.cycle_count = 0
        self.total_matches = 0
        self.start_time = time.time()
        
    def update_bot_state(self, bot_id: int, state: BotState, in_squad: bool = None):
        """Update a bot's state"""
        if bot_id in self.bots:
            self.bots[bot_id].state = state
            self.bots[bot_id].last_activity = time.time()
            if in_squad is not None:
                self.bots[bot_id].in_squad = in_squad
    
    async def wait_for_all_bots_ready(self, timeout: int = 30) -> bool:
        """Wait for all bots to be ready"""
        start = time.time()
        while time.time() - start < timeout:
            all_ready = all(bot.state in [BotState.IDLE, BotState.LOBBY] 
                          for bot in self.bots.values())
            if all_ready and len(self.bots) == self.total_bots:
                return True
            await asyncio.sleep(1)
        return False
    
    async def invite_squad_members(self, team_code: str) -> bool:
        """Squad builder invites other bots"""
        print(f"\n[ORCHESTRATOR] 🎯 Starting squad formation with code: {team_code}")
        self.current_team_code = team_code
        
        try:
            builder = self.bots[self.squad_builder_id]
            self.update_bot_state(self.squad_builder_id, BotState.INVITING)
            
            # Invite each member
            for member_id in range(1, self.total_bots + 1):
                if member_id == self.squad_builder_id:
                    continue
                
                print(f"[ORCHESTRATOR] 📧 BOT{self.squad_builder_id} inviting BOT{member_id}...")
                self.update_bot_state(member_id, BotState.INVITING)
                await asyncio.sleep(0.5)  # Stagger invites
                
                # Simulate invite acceptance
                self.update_bot_state(member_id, BotState.SQUAD_READY, in_squad=True)
                self.squad_members.append(member_id)
                print(f"[ORCHESTRATOR] ✅ BOT{member_id} joined squad")
                await asyncio.sleep(0.3)
            
            # Mark squad builder as in squad
            self.update_bot_state(self.squad_builder_id, BotState.SQUAD_READY, in_squad=True)
            self.squad_members.insert(0, self.squad_builder_id)
            self.active_squad = True
            
            print(f"[ORCHESTRATOR] ✅ Squad ready with {len(self.squad_members)} bots: {self.squad_members}")
            return True
            
        except Exception as e:
            print(f"[ORCHESTRATOR] ❌ Failed to form squad: {e}")
            self.update_bot_state(self.squad_builder_id, BotState.ERROR)
            return False
    
    async def start_match(self, spam_duration: int = 18) -> bool:
        """Start clash squad match"""
        print(f"\n[ORCHESTRATOR] 🎮 Starting match (spam: {spam_duration}s)...")
        
        if not self.active_squad:
            print("[ORCHESTRATOR] ❌ No active squad to start match")
            return False
        
        try:
            # All bots transition to match state
            for bot_id in self.squad_members:
                self.update_bot_state(bot_id, BotState.IN_MATCH)
            
            # Simulate spam for duration
            print(f"[ORCHESTRATOR] ⏳ Spamming auto-start packets...")
            await asyncio.sleep(spam_duration)
            
            print(f"[ORCHESTRATOR] ✅ Match started successfully")
            self.total_matches += 1
            return True
            
        except Exception as e:
            print(f"[ORCHESTRATOR] ❌ Failed to start match: {e}")
            return False
    
    async def wait_for_match_end(self, estimated_duration: int = 900) -> bool:
        """Wait for match to end"""
        print(f"\n[ORCHESTRATOR] ⏱️  Match in progress (est. {estimated_duration}s)...")
        
        try:
            # Simulate match duration
            # In real scenario, this would detect actual match end
            await asyncio.sleep(5)  # For demo, just wait 5 seconds
            
            print(f"[ORCHESTRATOR] 🏁 Match ended!")
            return True
            
        except Exception as e:
            print(f"[ORCHESTRATOR] ❌ Error during match: {e}")
            return False
    
    async def cleanup_squad(self, wait_before_leave: int = 5) -> bool:
        """Clean up squad after match"""
        print(f"\n[ORCHESTRATOR] 🧹 Cleaning up squad...")
        
        try:
            # Wait before leaving
            print(f"[ORCHESTRATOR] ⏳ Waiting {wait_before_leave}s before leaving...")
            await asyncio.sleep(wait_before_leave)
            
            # All bots leave squad
            for bot_id in self.squad_members:
                self.update_bot_state(bot_id, BotState.LOBBY, in_squad=False)
                await asyncio.sleep(0.2)
            
            self.active_squad = False
            self.squad_members.clear()
            
            print(f"[ORCHESTRATOR] ✅ All bots returned to lobby")
            return True
            
        except Exception as e:
            print(f"[ORCHESTRATOR] ❌ Failed to cleanup: {e}")
            return False
    
    async def recovery_mode(self, bot_id: int = None):
        """Recover from errors"""
        print(f"\n[ORCHESTRATOR] 🔄 RECOVERY MODE activated")
        
        if bot_id:
            print(f"[ORCHESTRATOR] 🔧 Recovering BOT{bot_id}...")
            self.bots[bot_id].error_count += 1
            self.update_bot_state(bot_id, BotState.IDLE)
            await asyncio.sleep(3)
            self.update_bot_state(bot_id, BotState.LOBBY)
        else:
            # Full system recovery
            print(f"[ORCHESTRATOR] 🔧 Full system recovery...")
            for bot_id in self.bots:
                self.bots[bot_id].state = BotState.IDLE
                await asyncio.sleep(0.5)
        
        print(f"[ORCHESTRATOR] ✅ Recovery complete")
    
    async def squad_cycle(self, team_code: str, spam_duration: int = 18, 
                         wait_after_match: int = 5, max_cycles: int = None):
        """Execute full squad cycle with error handling"""
        cycle = 0
        
        print(f"\n{'='*60}")
        print(f"[ORCHESTRATOR] 🚀 STARTING MULTI-BOT SQUAD CYCLES")
        print(f"{'='*60}")
        print(f"Total Bots: {self.total_bots}")
        print(f"Squad Builder: BOT{self.squad_builder_id}")
        print(f"{'='*60}\n")
        
        while max_cycles is None or cycle < max_cycles:
            cycle += 1
            
            print(f"\n{'▶'*30}")
            print(f"CYCLE {cycle} - START AT {time.strftime('%H:%M:%S')}")
            print(f"{'▶'*30}\n")
            
            try:
                # Wait for all bots to be ready
                if not await self.wait_for_all_bots_ready():
                    print("[ORCHESTRATOR] ⚠️  Not all bots ready, waiting...")
                    await self.recovery_mode()
                    continue
                
                # Form squad
                if not await self.invite_squad_members(team_code):
                    print("[ORCHESTRATOR] ⚠️  Squad formation failed, recovering...")
                    await self.recovery_mode()
                    continue
                
                await asyncio.sleep(2)
                
                # Start match
                if not await self.start_match(spam_duration):
                    print("[ORCHESTRATOR] ⚠️  Match start failed, recovering...")
                    await self.recovery_mode()
                    continue
                
                # Wait for match
                if not await self.wait_for_match_end():
                    await self.recovery_mode()
                    continue
                
                # Cleanup
                if not await self.cleanup_squad(wait_after_match):
                    await self.recovery_mode()
                    continue
                
                print(f"\n✅ CYCLE {cycle} COMPLETED")
                print(f"Total Matches: {self.total_matches}")
                print(f"{'◀'*30}\n")
                
                # Wait before next cycle
                print("[ORCHESTRATOR] ⏳ Waiting 3s before next cycle...")
                await asyncio.sleep(3)
                
            except Exception as e:
                print(f"[ORCHESTRATOR] ❌ Cycle error: {e}")
                await self.recovery_mode()
                await asyncio.sleep(5)
        
        print(f"\n{'='*60}")
        print(f"[ORCHESTRATOR] ✅ ALL CYCLES COMPLETE")
        print(f"Total Cycles: {cycle}")
        print(f"Total Matches: {self.total_matches}")
        print(f"Duration: {time.time() - self.start_time:.0f}s")
        print(f"{'='*60}\n")
    
    def get_summary(self) -> dict:
        """Get current operation summary"""
        return {
            'total_bots': self.total_bots,
            'active_squad': self.active_squad,
            'squad_members': self.squad_members,
            'squad_builder': self.squad_builder_id,
            'current_team_code': self.current_team_code,
            'cycle_count': self.cycle_count,
            'total_matches': self.total_matches,
            'uptime': time.time() - self.start_time,
            'bots_status': {
                bot_id: {
                    'state': bot.state.value,
                    'in_squad': bot.in_squad,
                    'errors': bot.error_count,
                    'matches': bot.match_count
                }
                for bot_id, bot in self.bots.items()
            }
        }
    
    async def safe_shutdown(self):
        """Safely shutdown all bots"""
        print("\n[ORCHESTRATOR] 🛑 Safe shutdown initiated...")
        
        if self.active_squad:
            await self.cleanup_squad(wait_before_leave=2)
        
        for bot_id in self.bots:
            self.update_bot_state(bot_id, BotState.IDLE)
        
        print("[ORCHESTRATOR] ✅ All bots safely stopped")

# Demo usage
async def demo():
    """Demo the orchestrator"""
    orchestrator = MultiBotsOrchestrator(total_bots=4)
    
    # Simulate bots being ready
    for i in range(1, 5):
        orchestrator.bots[i].uid = f"bot_uid_{i}"
        orchestrator.update_bot_state(i, BotState.LOBBY)
    
    # Run cycles
    await orchestrator.squad_cycle(
        team_code="123456",
        spam_duration=18,
        wait_after_match=5,
        max_cycles=2  # Demo: only 2 cycles
    )

if __name__ == "__main__":
    asyncio.run(demo())
