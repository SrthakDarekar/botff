# ⚡ QUICK START GUIDE - 4 Bots Auto Squad

## 5-Minute Setup

### 1️⃣ Add Your 4 Bot Accounts
Create file: `bot.txt`

```json
{
    "BOT1_UID": "BOT1_PASSWORD",
    "BOT2_UID": "BOT2_PASSWORD", 
    "BOT3_UID": "BOT3_PASSWORD",
    "BOT4_UID": "BOT4_PASSWORD"
}
```

**Example:**
```json
{
    "123456789": "mypassword1",
    "987654321": "mypassword2",
    "555666777": "mypassword3", 
    "888999000": "mypassword4"
}
```

### 2️⃣ Install Dependencies (if not done)
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Bot Launcher
```bash
python bot_launcher.py
```

### 4️⃣ Choose Option 1
```
Choose option (1-6): 1
📋 Enter Team Code for Squad: 123456
```

Done! ✅ Bots will continuously form squads and run matches.

---

## 🎮 Manual Control (Without Launcher)

### Option A: Run main.py directly
```bash
python main.py
```

Then message any bot:
```
/lw 123456    # Start auto with team code 123456
/stop_auto    # Stop all bots
/help         # Show menu
```

### Option B: Use launcher menu
```bash
python bot_launcher.py
# Choose option 2 for manual mode
```

---

## ✅ What Happens When You Run It

1. **Initialization** (30-60 seconds)
   - 4 bots authenticate with Garena
   - Bots connect to chat and online servers
   - Shows "[BOT1] ✅ Online - Ready"

2. **Squad Formation** (Automatic)
   - BOT1 sends squad invites to BOT2, BOT3, BOT4
   - All bots join
   - "✅ Squad formed with 4 bots"

3. **Match Starting**
   - BOT1 starts match with 18-second spam
   - "🎮 Match started"

4. **Match Plays**
   - Bots play clash squad
   - Match takes 10-30 minutes

5. **Lobby & Restart**
   - After match ends
   - Bots return to lobby (5 second wait)
   - Squad reforms automatically
   - Back to step 2 (LOOP)

---

## 🛠️ Common Settings

In `config.json`:

```json
{
    "total_bots": 4,              // ← Change if using less than 4
    "region": "IN",               // ← Change to your region
    "start_spam_duration": 18,    // ← Increase if match won't start
    "wait_after_match": 5         // ← Time before leaving squad
}
```

**Regions:**
- `IN` = India
- `BD` = Bangladesh
- `BR` = Brazil
- `US` = USA

---

## ❌ If Bots Don't Match

Try these steps:

1. **Check bot.txt is valid JSON**
   ```json
   {
       "UID": "PASSWORD",
       "UID2": "PASSWORD2"
   }
   ```

2. **Verify credentials work** (test in game manually)

3. **Restart with valid team code**
   ```
   /lw 123456
   ```

4. **Check if squad code is from a team room** (not random)

5. **Increase spam time in config.json**
   ```json
   "start_spam_duration": 25
   ```

---

## 📊 Monitor Status

In launcher menu → Option 4:
```
Squad Status: IN_MATCH
Total Bots: 4
Bots Joined: 4/4
Matches Completed: 3
Squad Builder: BOT1
```

---

## 🛑 Stop Bots

**Option 1: Via Launcher**
- Run `python bot_launcher.py`
- Choose option 5

**Option 2: Message Bot**
- Send message to any bot: `/stop_auto`

**Option 3: Keyboard**
- Press `Ctrl+C` to force stop

---

## 🎯 Tips for Success

✨ **Use a VPN** for better server connection  
✨ **Keep team code same** (don't change during run)  
✨ **Wait 2 minutes** after starting for all bots to initialize  
✨ **Test one bot first** before using 4  
✨ **Check internet connection** is stable  

---

## 📞 Still Having Issues?

1. Check [BOT_SETUP_4BOTS.md](BOT_SETUP_4BOTS.md) for detailed troubleshooting
2. Verify bot.txt has exactly 4 entries
3. Make sure all 4 accounts are verified in Free Fire
4. Try running with option 2 (manual) first to test connectivity

---

**You're all set! 🚀 Start with `python bot_launcher.py` now!**
