# 🎮 FREE FIRE 4-BOT AUTO SQUAD SYSTEM

**Complete automated solution for running 4 bots in Clash Squad with minimal setup**

## 📦 What's New

✨ **New Components:**
- `squad_manager.py` - Squad lifecycle management
- `bot_launcher.py` - Interactive menu for bot control  
- `multi_bot_orchestrator.py` - Advanced bot coordination
- `config.json` - Centralized configuration
- `QUICK_START.md` - Get running in 5 minutes
- `BOT_SETUP_4BOTS.md` - Detailed setup & troubleshooting

---

## 🚀 Start Here

### ⚡ 3-Step Quick Start
1. **Create `bot.txt`** with 4 bot credentials
2. **Run launcher:** `python bot_launcher.py`
3. **Choose option 1** → Enter team code → Done!

👉 **See [QUICK_START.md](QUICK_START.md) for detailed guide**

---

## 📊 System Overview

```
┌─────────────────────────────────────────┐
│      BOT LAUNCHER (bot_launcher.py)     │
│  - Interactive menu                     │
│  - Configuration management             │
│  - Status monitoring                    │
└────────────┬────────────────────────────┘
             │
     ┌───────┴───────┐
     ▼               ▼
┌─────────────┐  ┌──────────────────────────┐
│  main.py    │  │ squad_manager.py         │
│- Bot auth   │  │ - Squad formation        │
│- Connection │  │ - Match cycling          │
│- Commands   │  │ - Lobby management       │
└─────────────┘  └──────────────────────────┘
                       │
                       ▼
                 ┌─────────────────────┐
                 │ multi_bot_orchestrator.py
                 │ - Advanced coordination
                 │ - Error recovery
                 │ - State management
                 └─────────────────────┘
```

---

## 🎯 How It Works

### Auto Squad Mode (Recommended)
```
python bot_launcher.py → Option 1 → Team Code → ✅ Fully Automated
```
- BOT1 invites BOT2, BOT3, BOT4
- Matches start automatically
- After match: cleanup → new squad → repeat ∞

### Manual Mode
```
python main.py
/lw 123456     # Start with team code 123456
/stop_auto     # Stop all bots
```

### Orchestrator Mode (Advanced)
```python
from multi_bot_orchestrator import MultiBotsOrchestrator

orchestrator = MultiBotsOrchestrator(total_bots=4)
await orchestrator.squad_cycle(team_code="123456", max_cycles=10)
```

---

## 📁 File Structure

| File | Purpose |
|------|---------|
| `main.py` | Core bot engine (auth, connection, commands) |
| `squad_manager.py` | Squad operations & match cycling |
| `bot_launcher.py` | Interactive launcher with menu |
| `multi_bot_orchestrator.py` | Advanced multi-bot coordination |
| `config.json` | All configuration settings |
| `bot.txt` | Your 4 bot credentials (keep secret!) |
| `requirements.txt` | Python dependencies |
| `QUICK_START.md` | 5-minute setup guide |
| `BOT_SETUP_4BOTS.md` | Complete documentation |
| `MULTI_BOT_SETUP.md` | Original setup guide |

---

## ⚙️ Configuration

### Main Settings (config.json)

```json
{
    "total_bots": 4,
    "squad_builder_bot": 1,
    "region": "IN",
    "auto_cycle": true,
    "start_spam_duration": 18,
    "wait_after_match": 5
}
```

**Key Parameters:**
- `total_bots` - Number of bots (1-4)
- `squad_builder_bot` - Which bot invites others
- `region` - Server region (IN/BD/BR/US)
- `auto_cycle` - Enable continuous matching
- `start_spam_duration` - How long to spam match start
- `wait_after_match` - Wait time before leaving squad

---

## 🎮 Bot Commands

Message any online bot:

```
/lw <team_code>      - Start all 4 bots with squad
/stop_auto           - Stop all bot operations
/help                - Show command menu
/status              - Show current status
```

**Example:**
```
/lw 123456
```

---

## 🔧 Troubleshooting

### Bots won't authenticate
- ✅ Verify bot.txt has correct UIDs and passwords
- ✅ Test accounts work in Free Fire client
- ✅ Check Garena server status

### Squad won't form
- ✅ All 4 bots must be online
- ✅ Team code must be from a room (not random)
- ✅ BOT1 needs permission to invite

### Match won't start  
- ✅ Increase `start_spam_duration` to 25
- ✅ Check squad has all 4 members
- ✅ Verify correct room code

### Bots disconnect randomly
- ✅ Reduce `packet_delay`
- ✅ Increase `reconnect_delay`
- ✅ Check internet stability

👉 **Full troubleshooting: See [BOT_SETUP_4BOTS.md](BOT_SETUP_4BOTS.md#-troubleshooting)**

---

## 📊 Monitoring

### View Status
```bash
python bot_launcher.py → Option 4
```

Shows:
- Current squad status
- Bots joined count
- Matches completed
- Uptime

### Logs
Enable in config.json:
```json
"logging": {
    "enabled": true,
    "log_file": "bot_activity.log",
    "log_level": "DEBUG"
}
```

---

## 💡 Usage Scenarios

### Scenario 1: Continuous Farming (Recommended)
```bash
# Use launcher with auto-cycle
python bot_launcher.py
# Choose 1 → Enter team code → Walk away
```
✅ Bots continuously farm Clash Squad points

### Scenario 2: Quick Testing
```bash
python bot_launcher.py
# Choose 2 (manual mode)
# Send /lw <code> when ready
```
✅ Full control, test individual features

### Scenario 3: High-Volume Automation
```python
# Use orchestrator for advanced control
python  # Run in Python console
from multi_bot_orchestrator import MultiBotsOrchestrator
```
✅ Advanced features, error recovery, custom logic

---

## 🔐 Security

⚠️ **Important Reminders:**
- 🔒 Keep `bot.txt` secure and private
- 🤐 Don't share credentials or source code
- 🛡️ Use secondary/throwaway accounts for bots
- 📵 Don't run on shared computers

---

## 📈 Performance Tips

1. **Faster Matches** → Lower `wait_after_match`
2. **Reliable Connection** → Increase `reconnect_delay`
3. **Consistent Invites** → Lower `packet_delay`
4. **Better Stability** → Keep `start_spam_duration` at 18-20

---

## 🐛 Advanced Debug

### Enable Detailed Logging
```json
{
    "logging": {
        "enabled": true,
        "log_level": "DEBUG"
    }
}
```

### Custom Squad Cycles
```python
from squad_manager import SquadManager

manager = SquadManager(total_bots=4)
# Custom logic here
await manager.form_squad(team_code, key, iv, region, refs)
```

### Monitor Individual Bots
```bash
# Check bot.txt to see which UID corresponds to which bot
# Bots run in sequence: first UID = BOT1, second UID = BOT2, etc.
```

---

## ✨ Features Summary

✅ Fully Automated Squad Formation  
✅ Continuous Match Cycling  
✅ 4 Concurrent Bots  
✅ Error Recovery & Reconnection  
✅ Interactive Launcher Menu  
✅ Configuration Management  
✅ Status Monitoring  
✅ Command-Based Control  
✅ Advanced Orchestration  
✅ Comprehensive Documentation  

---

## 🚀 Getting Started

### First Time Users
1. Read [QUICK_START.md](QUICK_START.md) (5 min)
2. Create `bot.txt` with 4 credentials
3. Run `python bot_launcher.py`
4. Choose option 1
5. Enter team code

### Experienced Users
1. Configure `config.json` as needed
2. Run `python bot_launcher.py`
3. Use menu or direct commands

### Advanced Users
1. Import `multi_bot_orchestrator.py` in custom scripts
2. Implement custom squad logic
3. Use API functions directly

---

## 📞 Quick Help

**Q: How do I update the team code?**
A: Edit `config.json` or send new `/lw <code>` command

**Q: Can I use less than 4 bots?**
A: Yes, change `total_bots` in config.json

**Q: Will bots automatically restart matches?**
A: Yes if `auto_cycle: true` in config

**Q: How long does each cycle take?**
A: ~15-30 minutes (depends on match duration)

---

## 📋 File Checklist

Before running, ensure you have:
- ✅ `main.py` - Original bot engine
- ✅ `bot.txt` - 4 bot credentials
- ✅ `squad_manager.py` - NEW squad operations
- ✅ `bot_launcher.py` - NEW interactive launcher  
- ✅ `multi_bot_orchestrator.py` - NEW advanced orchestration
- ✅ `config.json` - NEW configuration file
- ✅ All `.py` files from `Pb2/` directory
- ✅ `requirements.txt` dependencies installed

---

## 🎯 Next Steps

1. **Setup:** Follow [QUICK_START.md](QUICK_START.md)
2. **Run:** `python bot_launcher.py`
3. **Choose:** Option 1 (Auto) or 2 (Manual)
4. **Enjoy:** Automated Clash Squad farming! 🎮

---

**Built with ❤️ for Free Fire Automation**

*Last Updated: 2026*
