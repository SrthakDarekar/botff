# 🤖 Multi-Bot Setup Guide (4 Bots Clash Squad Auto)

## Overview
This updated version supports **4 concurrent bots** that automatically join the same squad, spam auto-start after match begins, and restart continuously after each match ends.

## Features
✅ 4 bots running in parallel  
✅ Automatic squad joining with team code  
✅ Continuous auto-start spam (18 seconds)  
✅ Automatic restart after match ends (5 seconds wait)  
✅ Single command to start all bots  
✅ Single command to stop all bots  
✅ Synchronized team operation  

## Setup Instructions

### Step 1: Prepare Bot Credentials
Create a file named `bot.txt` in the same directory as `main.py`:

```json
{
    "UID1": "PASSWORD1",
    "UID2": "PASSWORD2",
    "UID3": "PASSWORD3",
    "UID4": "PASSWORD4"
}
```

**Important:**
- Replace `UID1`, `UID2`, `UID3`, `UID4` with actual Free Fire bot UIDs
- Replace `PASSWORD1`, `PASSWORD2`, `PASSWORD3`, `PASSWORD4` with their respective passwords
- Use exactly 4 credentials or adjust `TOTAL_BOTS` in main.py if needed
- Keep the JSON format valid (no trailing commas)

### Step 2: Run the Script
```bash
python main.py
```

### Step 3: Wait for Initialization
The script will:
1. Load all 4 bot credentials from `bot.txt`
2. Authenticate each bot with Free Fire servers
3. Connect to chat and online servers
4. Show status: `[BOT1] ✅ Online - Ready for commands`

### Step 4: Start Auto Squad
Send message to any bot:
```
/lw TEAMCODE
```

Example:
```
/lw 12345678
```

**What happens:**
- All 4 bots join the squad with team code `12345678`
- Each bot spams auto-start packets for 18 seconds
- After match ends, bots automatically restart and rejoin
- Cycle repeats until you send `/stop_auto`

### Step 5: Stop All Bots
Send message to any bot:
```
/stop_auto
```

## Commands

| Command | Description |
|---------|-------------|
| `/lw <TEAMCODE>` | Start all 4 bots with team code |
| `/stop_auto` | Stop all bots |
| `/help` or `/menu` | Show command list |

## Output Example
```
🚀 Starting 4 bots...
[BOT1] 🔐 Logging in with UID: XXXX
[BOT2] 🔐 Logging in with UID: XXXX
[BOT3] 🔐 Logging in with UID: XXXX
[BOT4] 🔐 Logging in with UID: XXXX
[BOT1] ✅ Online - Ready for commands
[BOT2] ✅ Online - Ready for commands
[BOT3] ✅ Online - Ready for commands
[BOT4] ✅ Online - Ready for commands
✅ All 4 bots ready! Use /lw <team_code> to start

[BOT1] Joined squad with team code: 12345678
[BOT2] Joined squad with team code: 12345678
[BOT3] Joined squad with team code: 12345678
[BOT4] Joined squad with team code: 12345678
[BOT1] Auto-start spam finished
[BOT1] Left squad
[BOT1] ✅ Match cycle 1 completed. Restarting in 3 seconds...
...
```

## Configuration Options

### Total Bots
Edit `main.py` line ~248:
```python
TOTAL_BOTS = 4  # Change this number (e.g., 2, 3, 5, etc.)
```

### Match Duration
Edit `main.py` line ~245:
```python
start_spam_duration = 18  # Duration of auto-start spam (seconds)
wait_after_match = 5      # Wait time after match ends (seconds)
```

### Spam Delay
Edit `main.py` line ~246:
```python
start_spam_delay = 0.1    # Delay between spam packets (seconds)
```

## Troubleshooting

### Bot doesn't join squad
- Check team code is correct and 8 digits
- Verify bot credentials in `bot.txt`
- Make sure bots are authorized in the squad

### Bots stop after first match
- Check console for error messages
- Verify internet connection is stable
- Check if bot accounts have been banned

### Only 1-2 bots connect
- Check if all 4 UIDs are valid
- Verify JSON format in `bot.txt`
- Look for "Failed to initialize" messages

### High CPU/Memory usage
- Reduce number of bots: `TOTAL_BOTS = 2`
- Increase `start_spam_delay` to 0.2 or higher
- Close other applications

## Performance Tips
1. Use stronger internet connection
2. Place bots in geographically close regions
3. Stagger bot login times (already done with 2-second delay)
4. Monitor memory usage with Task Manager

## Support
Developer: @lsahilxx  
For issues or updates, contact developer
