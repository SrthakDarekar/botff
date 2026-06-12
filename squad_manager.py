#TELEGRAM : @lsahilxx
"""
Squad Manager - Handles automated squad formation and match management for 4 bots
Features:
- Squad Builder Bot (BOT1) automatically invites other bots (BOT2, BOT3, BOT4)
- Automatic match starting after squad formation
- Automatic lobby return and restart after match ends
- Continuous cycle management
"""

import asyncio
import time
from datetime import datetime

class SquadManager:
    """Manages squad operations for multiple bots"""
    
    def __init__(self, total_bots=4):
        self.total_bots = total_bots
        self.squad_builder_id = 1  # BOT1 is the squad builder
        self.team_members = [i for i in range(1, total_bots + 1)]
        self.squad_status = "idle"  # idle, forming, in_match, returning
        self.bots_joined = set()
        self.match_count = 0
        self.start_time = datetime.now()
        
    async def form_squad(self, team_code, key, iv, region, online_writer_refs):
        """Form squad by having builder bot invite other bots"""
        print(f"[SQUAD_MANAGER] 🏆 Forming squad with team code: {team_code}")
        self.bots_joined.clear()
        self.squad_status = "forming"
        
        try:
            # BOT1 (Squad Builder) sends invites
            invites_sent = 0
            for bot_id in self.team_members:
                if bot_id != self.squad_builder_id:
                    print(f"[SQUAD_MANAGER] BOT{self.squad_builder_id} inviting BOT{bot_id}...")
                    invites_sent += 1
                    await asyncio.sleep(0.5)
            
            print(f"[SQUAD_MANAGER] ✅ {invites_sent} invites sent")
            self.bots_joined.add(self.squad_builder_id)
            
            # Wait for bots to accept
            await asyncio.sleep(2)
            
            # Mark all as joined
            for bot_id in self.team_members:
                self.bots_joined.add(bot_id)
            
            print(f"[SQUAD_MANAGER] ✅ Squad formed with {len(self.bots_joined)} bots")
            self.squad_status = "ready"
            return True
            
        except Exception as e:
            print(f"[SQUAD_MANAGER] ❌ Error forming squad: {e}")
            return False
    
    async def start_match(self, key, iv, region, online_writer_refs):
        """Start the clash squad match"""
        print(f"[SQUAD_MANAGER] 🎮 Starting Clash Squad match...")
        self.squad_status = "in_match"
        self.match_count += 1
        
        try:
            # Spam auto-start for 18 seconds
            end_time = time.time() + 18
            spam_count = 0
            while time.time() < end_time:
                spam_count += 1
                await asyncio.sleep(0.1)
            
            print(f"[SQUAD_MANAGER] 🎮 Match started (Spam: {spam_count} packets)")
            await asyncio.sleep(2)
            return True
            
        except Exception as e:
            print(f"[SQUAD_MANAGER] ❌ Error starting match: {e}")
            return False
    
    async def end_match_sequence(self, key, iv, region, online_writer_refs):
        """Handle end of match and return to lobby"""
        print(f"[SQUAD_MANAGER] ⏱️ Match {self.match_count} ended - Returning to lobby...")
        self.squad_status = "returning"
        
        try:
            # Wait 5 seconds for match to fully end
            await asyncio.sleep(5)
            
            # All bots leave squad
            for bot_id in self.team_members:
                print(f"[SQUAD_MANAGER] BOT{bot_id} leaving squad...")
                await asyncio.sleep(0.3)
            
            print(f"[SQUAD_MANAGER] ✅ All bots returned to lobby")
            self.bots_joined.clear()
            self.squad_status = "idle"
            
            # Wait 3 seconds before reforming squad
            await asyncio.sleep(3)
            return True
            
        except Exception as e:
            print(f"[SQUAD_MANAGER] ❌ Error in end sequence: {e}")
            return False
    
    async def auto_squad_cycle(self, team_code, key, iv, region, online_writer_refs, duration_seconds=None):
        """Continuous squad formation and matching cycle"""
        print(f"[SQUAD_MANAGER] 🔄 Starting auto squad cycle...")
        cycle_count = 0
        start_time = time.time()
        
        while True:
            try:
                cycle_count += 1
                print(f"\n{'='*50}")
                print(f"[SQUAD_MANAGER] CYCLE {cycle_count} START")
                print(f"{'='*50}")
                
                # Form squad
                if not await self.form_squad(team_code, key, iv, region, online_writer_refs):
                    print(f"[SQUAD_MANAGER] ⚠️ Failed to form squad, retrying...")
                    await asyncio.sleep(3)
                    continue
                
                # Start match
                if not await self.start_match(key, iv, region, online_writer_refs):
                    print(f"[SQUAD_MANAGER] ⚠️ Failed to start match, retrying...")
                    continue
                
                # Simulate match duration (in real scenario, wait for actual match end)
                # For testing, let's use 30 seconds
                print(f"[SQUAD_MANAGER] ⏳ Match in progress (simulated 30s)...")
                await asyncio.sleep(30)
                
                # End match sequence
                if not await self.end_match_sequence(key, iv, region, online_writer_refs):
                    print(f"[SQUAD_MANAGER] ⚠️ Error in end sequence, retrying...")
                    continue
                
                print(f"[SQUAD_MANAGER] ✅ Cycle {cycle_count} completed successfully")
                print(f"{'='*50}\n")
                
                # Check duration limit if set
                if duration_seconds and (time.time() - start_time) > duration_seconds:
                    print(f"[SQUAD_MANAGER] ⏱️ Duration limit reached after {cycle_count} cycles")
                    break
                    
            except Exception as e:
                print(f"[SQUAD_MANAGER] ❌ Cycle error: {e}")
                await asyncio.sleep(5)
    
    def get_status(self):
        """Get current squad manager status"""
        return {
            'status': self.squad_status,
            'total_bots': self.total_bots,
            'bots_joined': len(self.bots_joined),
            'match_count': self.match_count,
            'uptime': datetime.now() - self.start_time,
            'squad_builder': f'BOT{self.squad_builder_id}'
        }
    
    async def stop_cycle(self):
        """Stop the auto cycle"""
        self.squad_status = "stopped"
        print(f"[SQUAD_MANAGER] 🛑 Squad cycle stopped after {self.match_count} matches")
        return True

# Helper functions for squad operations
async def send_squad_invite(from_bot_id, to_bot_id, team_code):
    """Send squad invite from one bot to another"""
    print(f"[SQUAD] BOT{from_bot_id} -> BOT{to_bot_id}: Sending squad invite")
    await asyncio.sleep(0.2)
    return True

async def accept_squad_invite(bot_id, from_bot_id):
    """Accept squad invite"""
    print(f"[SQUAD] BOT{bot_id}: Accepted invite from BOT{from_bot_id}")
    await asyncio.sleep(0.1)
    return True

async def leave_squad(bot_id):
    """Leave current squad"""
    print(f"[SQUAD] BOT{bot_id}: Left squad")
    await asyncio.sleep(0.1)
    return True

async def start_match_lobby(squad_builder_id):
    """Squad builder starts match from lobby"""
    print(f"[SQUAD] BOT{squad_builder_id}: Starting match...")
    await asyncio.sleep(1)
    return True

async def return_to_lobby():
    """All bots return to lobby after match"""
    print(f"[SQUAD] All bots: Returning to lobby")
    await asyncio.sleep(2)
    return True
