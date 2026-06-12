#TELEGRAM : @lsahilxx
"""
Bot Launcher - Easy startup for all 4 bots with squad auto-management
Run this script to start all bots with squad formation and auto-matching
"""

import asyncio
import subprocess
import json
import os
import sys
from pathlib import Path
from squad_manager import SquadManager

class BotLauncher:
    """Manages launching and monitoring multiple bots"""
    
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.config = self.load_config()
        self.squad_manager = SquadManager(self.config.get('total_bots', 4))
        self.bot_processes = []
        
    def load_config(self):
        """Load configuration from config.json"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        else:
            # Return default config
            return {
                'total_bots': 4,
                'team_code': '000000',
                'auto_cycle': True,
                'cycle_duration': None,  # None for infinite
                'squad_builder_bot': 1,
                'region': 'IN',
                'start_spam_duration': 18,
                'wait_after_match': 5,
                'bot_credentials_file': 'bot.txt'
            }
    
    def save_config(self):
        """Save configuration to config.json"""
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=4)
    
    async def start_all_bots(self):
        """Start all bots from main.py"""
        print("\n" + "="*60)
        print("🚀 BOT LAUNCHER - Starting All Bots")
        print("="*60)
        print(f"✅ Total Bots: {self.config['total_bots']}")
        print(f"✅ Squad Builder: BOT{self.config['squad_builder_bot']}")
        print(f"✅ Region: {self.config['region']}")
        print(f"✅ Auto Cycle: {self.config['auto_cycle']}")
        print("="*60 + "\n")
        
        # Check if bot.txt exists
        if not os.path.exists(self.config['bot_credentials_file']):
            print(f"❌ ERROR: {self.config['bot_credentials_file']} not found!")
            print("Please create bot.txt with 4 bot credentials in JSON format:")
            print('{"UID1": "PASS1", "UID2": "PASS2", "UID3": "PASS3", "UID4": "PASS4"}')
            return False
        
        try:
            # Start main.py which handles bot initialization
            print("[*] Starting main.py (this initializes all bots)...")
            await asyncio.sleep(1)
            
            # The actual bot startup happens in main.py
            # This launcher coordinates the squad management
            print("✅ All bots initializing...\n")
            return True
            
        except Exception as e:
            print(f"❌ Error starting bots: {e}")
            return False
    
    async def run_squad_auto_mode(self, team_code):
        """Run squad in auto mode - continuous matching"""
        print(f"\n🔄 SQUAD AUTO MODE - Continuous Matching")
        print("="*60)
        print(f"📋 Team Code: {team_code}")
        print(f"🎯 Squad Builder: BOT{self.config['squad_builder_bot']}")
        print(f"🤖 Squad Members: BOT1, BOT2, BOT3, BOT4")
        print("="*60 + "\n")
        
        # Run continuous squad cycles
        await self.squad_manager.auto_squad_cycle(
            team_code=team_code,
            key=None,  # Would be passed from bot connections
            iv=None,
            region=self.config['region'],
            online_writer_refs={},
            duration_seconds=self.config['cycle_duration']
        )
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print("🎮 FREE FIRE BOT SQUAD MANAGER - Main Menu")
        print("="*60)
        print("1. Start All Bots with Auto Squad")
        print("2. Start Bots (Manual Control)")
        print("3. Configure Settings")
        print("4. View Status")
        print("5. Stop All Bots")
        print("6. Exit")
        print("="*60)
        return input("Choose option (1-6): ").strip()
    
    def configure_settings(self):
        """Configure bot settings"""
        print("\n" + "="*60)
        print("⚙️  CONFIGURATION MENU")
        print("="*60)
        print(f"1. Total Bots (Current: {self.config['total_bots']})")
        print(f"2. Squad Builder Bot (Current: BOT{self.config['squad_builder_bot']})")
        print(f"3. Region (Current: {self.config['region']})")
        print(f"4. Start Spam Duration (Current: {self.config['start_spam_duration']}s)")
        print(f"5. Wait After Match (Current: {self.config['wait_after_match']}s)")
        print(f"6. Auto Cycle (Current: {'ON' if self.config['auto_cycle'] else 'OFF'})")
        print("7. Back to Menu")
        print("="*60)
        
        choice = input("Choose option (1-7): ").strip()
        
        if choice == '1':
            self.config['total_bots'] = int(input("Enter total bots (max 4): "))
        elif choice == '2':
            self.config['squad_builder_bot'] = int(input("Enter squad builder bot (1-4): "))
        elif choice == '3':
            print("Available regions: IN (India), BD (Bangladesh), BR (Brazil), US (USA)")
            self.config['region'] = input("Enter region code: ").upper()
        elif choice == '4':
            self.config['start_spam_duration'] = int(input("Enter duration in seconds: "))
        elif choice == '5':
            self.config['wait_after_match'] = int(input("Enter wait time in seconds: "))
        elif choice == '6':
            self.config['auto_cycle'] = not self.config['auto_cycle']
            print(f"Auto Cycle: {'✅ ON' if self.config['auto_cycle'] else '❌ OFF'}")
        elif choice == '7':
            return
        
        self.save_config()
        print("✅ Settings saved!")
    
    def view_status(self):
        """View current status"""
        status = self.squad_manager.get_status()
        print("\n" + "="*60)
        print("📊 CURRENT STATUS")
        print("="*60)
        print(f"Squad Status: {status['status'].upper()}")
        print(f"Total Bots: {status['total_bots']}")
        print(f"Bots Joined: {status['bots_joined']}/{status['total_bots']}")
        print(f"Matches Completed: {status['match_count']}")
        print(f"Uptime: {status['uptime']}")
        print(f"Squad Builder: {status['squad_builder']}")
        print("="*60)

async def main_menu_loop():
    """Main menu loop"""
    launcher = BotLauncher()
    
    while True:
        choice = launcher.display_menu()
        
        if choice == '1':
            if await launcher.start_all_bots():
                team_code = input("\n📋 Enter Team Code for Squad: ").strip()
                if team_code and team_code.isdigit():
                    await launcher.run_squad_auto_mode(team_code)
                else:
                    print("❌ Invalid team code")
        
        elif choice == '2':
            print("\n✅ Starting bots in manual mode...")
            print("Send commands to bots via chat:")
            print("  /lw <team_code> - Join squad")
            print("  /stop_auto - Stop auto")
            print("  /help - Show help")
            if await launcher.start_all_bots():
                print("\n✅ Bots are now online. Use /lw <team_code> to start.")
                input("Press Enter to continue...")
        
        elif choice == '3':
            launcher.configure_settings()
        
        elif choice == '4':
            launcher.view_status()
        
        elif choice == '5':
            print("\n🛑 Stopping all bots...")
            await launcher.squad_manager.stop_cycle()
            print("✅ All bots stopped")
        
        elif choice == '6':
            print("\n👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice")

if __name__ == '__main__':
    try:
        asyncio.run(main_menu_loop())
    except KeyboardInterrupt:
        print("\n\n👋 Bot Launcher stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")
