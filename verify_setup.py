#TELEGRAM : @lsahilxx
"""
Bot System Verifier - Check if everything is ready before running
Verifies: bot.txt, config.json, dependencies, file structure
"""

import os
import json
import sys
from pathlib import Path

class BotSystemVerifier:
    """Verify bot system setup"""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.success = []
        self.workspace_path = Path.cwd()
        
    def verify_all(self):
        """Run all verifications"""
        print("\n" + "="*60)
        print("🔍 BOT SYSTEM VERIFIER")
        print("="*60 + "\n")
        
        self.check_python_version()
        self.check_files_exist()
        self.check_bot_txt()
        self.check_config_json()
        self.check_dependencies()
        self.check_protobuf_files()
        
        self.print_results()
        return len(self.errors) == 0
    
    def check_python_version(self):
        """Check Python version"""
        version = sys.version_info
        if version.major >= 3 and version.minor >= 8:
            self.success.append(f"✅ Python {version.major}.{version.minor} (OK)")
        else:
            self.errors.append(f"❌ Python {version.major}.{version.minor} (Need 3.8+)")
    
    def check_files_exist(self):
        """Check all required files exist"""
        required_files = {
            'main.py': 'Main bot engine',
            'autoup.py': 'Auto update module',
            'xDL.py': 'Download utility',
            'squad_manager.py': 'Squad operations (NEW)',
            'bot_launcher.py': 'Bot launcher (NEW)',
            'multi_bot_orchestrator.py': 'Bot orchestrator (NEW)',
            'config.json': 'Configuration (NEW)',
            'requirements.txt': 'Dependencies',
            'bot.txt.example': 'Bot credentials template'
        }
        
        for filename, description in required_files.items():
            filepath = self.workspace_path / filename
            if filepath.exists():
                self.success.append(f"✅ {filename} - {description}")
            else:
                self.errors.append(f"❌ {filename} NOT FOUND - {description}")
    
    def check_bot_txt(self):
        """Check bot.txt configuration"""
        bot_file = self.workspace_path / "bot.txt"
        
        if not bot_file.exists():
            self.warnings.append("⚠️  bot.txt not found - Create it from bot.txt.example")
            return
        
        try:
            with open(bot_file, 'r') as f:
                bots = json.load(f)
            
            bot_count = len(bots)
            if bot_count < 4:
                self.warnings.append(f"⚠️  Only {bot_count} bots in bot.txt (expected 4)")
            elif bot_count == 4:
                self.success.append(f"✅ bot.txt has 4 bot credentials")
            else:
                self.warnings.append(f"⚠️  bot.txt has {bot_count} bots (only first 4 used)")
            
            # Validate JSON format
            all_strings = all(isinstance(k, str) and isinstance(v, str) 
                            for k, v in bots.items())
            if all_strings:
                self.success.append("✅ bot.txt is valid JSON with string values")
            else:
                self.errors.append("❌ bot.txt format invalid - needs string UID/password pairs")
                
        except json.JSONDecodeError as e:
            self.errors.append(f"❌ bot.txt JSON error: {e}")
        except Exception as e:
            self.errors.append(f"❌ Error reading bot.txt: {e}")
    
    def check_config_json(self):
        """Check config.json"""
        config_file = self.workspace_path / "config.json"
        
        if not config_file.exists():
            self.warnings.append("⚠️  config.json not found - Will use defaults")
            return
        
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
            
            required_keys = ['total_bots', 'squad_builder_bot', 'region']
            missing_keys = [k for k in required_keys if k not in config]
            
            if missing_keys:
                self.warnings.append(f"⚠️  config.json missing keys: {missing_keys}")
            else:
                self.success.append("✅ config.json is valid and complete")
            
            # Validate values
            if config.get('total_bots', 0) > 4:
                self.errors.append("❌ config.json total_bots > 4 (not supported)")
            if config.get('squad_builder_bot', 0) > 4:
                self.errors.append("❌ config.json squad_builder_bot > 4 (not supported)")
                
        except json.JSONDecodeError as e:
            self.errors.append(f"❌ config.json JSON error: {e}")
        except Exception as e:
            self.errors.append(f"❌ Error reading config.json: {e}")
    
    def check_dependencies(self):
        """Check if required Python packages are installed"""
        required_packages = [
            ('requests', 'HTTP requests'),
            ('aiohttp', 'Async HTTP'),
            ('google', 'Google protobuf'),
            ('Crypto', 'PyCryptodome'),
            ('jwt', 'PyJWT'),
            ('urllib3', 'URL utilities'),
            ('pytz', 'Timezone support'),
            ('protobuf_decoder', 'Protobuf decoder'),
        ]
        
        missing = []
        for package, description in required_packages:
            try:
                __import__(package)
                self.success.append(f"✅ {package} ({description})")
            except ImportError:
                missing.append(f"{package} ({description})")
        
        if missing:
            for pkg_desc in missing:
                self.warnings.append(f"⚠️  {pkg_desc} not installed")
            self.warnings.append("   Run: pip install -r requirements.txt")
    
    def check_protobuf_files(self):
        """Check protobuf compiled files"""
        pb2_dir = self.workspace_path / "Pb2"
        
        if not pb2_dir.exists():
            self.errors.append("❌ Pb2/ directory not found")
            return
        
        required_pb2_files = [
            'DEcwHisPErMsG_pb2.py',
            'MajoRLoGinrEq_pb2.py',
            'MajoRLoGinrEs_pb2.py',
            'PorTs_pb2.py'
        ]
        
        missing_pb2 = []
        for filename in required_pb2_files:
            filepath = pb2_dir / filename
            if filepath.exists():
                self.success.append(f"✅ Pb2/{filename}")
            else:
                missing_pb2.append(filename)
        
        if missing_pb2:
            for filename in missing_pb2:
                self.errors.append(f"❌ Pb2/{filename} NOT FOUND")
        else:
            self.success.append("✅ All protobuf files present")
    
    def print_results(self):
        """Print verification results"""
        print("\n" + "="*60)
        print("📊 VERIFICATION RESULTS")
        print("="*60 + "\n")
        
        if self.success:
            print("✅ SUCCESS:")
            for msg in self.success:
                print(f"   {msg}")
        
        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for msg in self.warnings:
                print(f"   {msg}")
        
        if self.errors:
            print("\n❌ ERRORS:")
            for msg in self.errors:
                print(f"   {msg}")
        
        print("\n" + "="*60)
        
        if not self.errors and not self.warnings:
            print("✅ SYSTEM READY! You can run bots now.")
            print("   Command: python bot_launcher.py")
        elif not self.errors:
            print("⚠️  SYSTEM PARTIALLY READY (fix warnings)")
            print("   Command: python bot_launcher.py")
        else:
            print("❌ SYSTEM NOT READY (fix errors first)")
        
        print("="*60 + "\n")

def main():
    """Run verifier"""
    verifier = BotSystemVerifier()
    ready = verifier.verify_all()
    
    if ready:
        print("🚀 Ready to launch bots!")
        print("   Run: python bot_launcher.py\n")
        return 0
    else:
        print("🔧 Fix errors above and try again.\n")
        return 1

if __name__ == '__main__':
    exit(main())
