# 🤖 4-Bot Automated Squad System for Free Fire Clash Squad

## 📋 Overview
This system allows you to run **4 bots simultaneously** that:
- ✅ Automatically form squads (BOT1 invites BOT2, BOT3, BOT4)
- ✅ Join each other in Clash Squad matches
- ✅ Start matches automatically with spam-start
- ✅ Complete matches and return to lobby
- ✅ Start new matches on continuous loop
- ✅ Fully automated with minimal manual intervention

## 🎯 System Components

### Core Files
| File | Purpose |
|------|---------|
| `main.py` | Bot login, server connection, command handling |
| `squad_manager.py` | Squad formation, match management, cycles |
| `bot_launcher.py` | Menu-driven interface for bot control |
| `config.json` | Configuration for all bots |
| `bot.txt` | Bot credentials (4 accounts) |

### Bot Roles
- **BOT1** (Squad Builder): Invites other bots, starts matches
- **BOT2, BOT3, BOT4** (Squad Members): Accept invites, follow builder

---

## 🚀 Setup Instructions

### Step 1: Prepare Bot Accounts
You need **4 Free Fire accounts**. Create them via:
- Garena Connect
- Facebook Login
- Google Play Account

### Step 2: Create `bot.txt`
Copy [bot.txt.example](bot.txt.example) to `bot.txt` and add your credentials:

```json
{
    "UID1": "PASSWORD1",
    "UID2": "PASSWORD2", 
    "UID3": "PASSWORD3",
    "UID4": "PASSWORD4"
}
```

**Important:**
- Use actual Free Fire UIDs (not usernames)
- Use corresponding Garena passwords
- Keep JSON format valid (no trailing commas)
- Order matters: BOT1 is squad builder

### Step 3: Verify Dependencies
Install required packages:
```bash
pip install -r requirements.txt
```

### Step 4: Update Region (Optional)
Edit `config.json` and set your region:
```json
"region": "IN"
```

Available regions:
- `IN` - India
- `BD` - Bangladesh  
- `BR` - Brazil
- `US` - USA
- `TW` - Taiwan

---

## 🎮 Running the System

### Method 1: Using Bot Launcher (Recommended)
```bash
python bot_launcher.py
```

Menu options:
- **Option 1**: Start all bots with auto squad (full auto mode)
- **Option 2**: Start bots in manual mode (you send commands)
- **Option 3**: Configure settings
- **Option 4**: View current status
- **Option 5**: Stop all bots
- **Option 6**: Exit

### Method 2: Direct main.py with Manual Commands
```bash
python main.py
```

Then message any bot:
```
/lw <team_code>    # Start all 4 bots with squad code
/stop_auto         # Stop all bots
/help              # Show available commands
```

### Method 3: Auto Script (runs continuously)
```bash
python bot_launcher.py
# Choose option 1 → Enter team code → Fully automated
```

---

## 📊 Workflow Diagram

```
[Start] 
  ↓
[All 4 Bots Online]
  ↓
[BOT1 Forms Squad - Invites BOT2, BOT3, BOT4]
  ↓
[All Bots Accept & Join Squad]
  ↓
[BOT1 Starts Match (18 second spam-start)]
  ↓
[Clash Squad Match Begins]
  ↓
[Match Plays for 10-20 minutes]
  ↓
[Match Ends]
  ↓
[Wait 5 seconds for cleanup]
  ↓
[All Bots Leave Squad]
  ↓
[Return to Lobby]
  ↓
[Wait 3 seconds]
  ↓
[LOOP → Form New Squad & Restart]
```

---

## ⚙️ Configuration Options

### config.json Settings

```json
{
    "total_bots": 4,                    // Number of bots (1-4)
    "squad_builder_bot": 1,             // Which bot invites others (1-4)
    "region": "IN",                     // Server region
    "auto_cycle": true,                 // Enable continuous cycling
    "cycle_duration": null,             // null = infinite, or seconds
    
    "start_spam_duration": 18,          // How long to spam start (seconds)
    "wait_after_match": 5,              // Wait before leaving squad (seconds)
    
    "squad_settings": {
        "auto_accept_invites": true,    // Auto accept squad invites
        "auto_ready_up": true,          // Auto ready after joining
        "prevent_squad_leave": false    // Keep squad locked
    }
}
```

---

## 🔧 Troubleshooting

### ❌ "bot.txt not found"
**Solution**: Create bot.txt with 4 credentials in JSON format

### ❌ "Invalid credentials" 
**Solution**: 
- Verify UID is correct (not username)
- Check password matches Garena account
- Ensure account is not banned

### ❌ Bots connect but don't match
**Solution**:
- Send `/lw <valid_team_code>` to start squad
- Check if BOT1 can invite (may need friend status)
- Verify all 4 bots are online

### ❌ Match doesn't start
**Solution**:
- Increase `start_spam_duration` to 25 seconds
- Ensure squad has 4 members
- Check region setting matches server

### ❌ Bots disconnect randomly
**Solution**:
- Reduce `packet_delay` in config
- Increase `reconnect_delay` 
- Check internet stability

---

## 📱 Bot Commands

Send these messages to any online bot:

| Command | Effect |
|---------|--------|
| `/lw <code>` | All bots join team code |
| `/stop_auto` | Stop all bot operations |
| `/help` | Show help menu |
| `/status` | Show bot status |

---

## 🔐 Security Notes

⚠️ **Important:**
- Keep bot.txt secure - don't share
- Use throwaway/secondary accounts for bots
- Store credentials safely
- Don't run on shared computers

---

## 📈 Performance Tips

1. **Faster Matches**: Lower `wait_after_match` value
2. **More Reliable**: Increase `reconnect_delay` 
3. **Faster Invites**: Lower `packet_delay`
4. **Stable Connection**: Keep `start_spam_duration` at 18-20

---

## 🐛 Debug Mode

Enable logging to see detailed bot activity:

```json
"logging": {
    "enabled": true,
    "log_file": "bot_activity.log",
    "log_level": "DEBUG"
}
```

Then check `bot_activity.log` for detailed logs.

---

## 📞 Support

If bots aren't working:
1. Check all 4 accounts are active
2. Verify network connection
3. Restart the script
4. Check for Garena server status
5. Try with different team code

---

## ✨ Features

✅ 4 Concurrent Bots  
✅ Automatic Squad Formation  
✅ Continuous Match Cycling  
✅ Auto Restart After Match  
✅ Menu-Driven Launcher  
✅ Configuration Management  
✅ Status Monitoring  
✅ Error Recovery  

---

## 📝 Notes

- First run takes 30-60 seconds for authentication
- Each match cycle takes 15-30 minutes
- Bots reconnect automatically on disconnect
- All 4 bots must be online before squad can form
- Squad code must be valid for team (room ID)

**Happy Botting! 🎮**
