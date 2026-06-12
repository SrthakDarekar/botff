#TELEGRAM : @lsahilxx
import requests, os, json, binascii, time, urllib3, base64, datetime, re, socket, ssl, asyncio, aiohttp, random, traceback
from protobuf_decoder.protobuf_decoder import Parser
from xDL import *
from autoup import *
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from Pb2 import DEcwHisPErMsG_pb2, MajoRLoGinrEs_pb2, PorTs_pb2, MajoRLoGinrEq_pb2
import google.protobuf.json_format as json_format

def rot13(text):
    result = ""
    for c in text:
        if 'a' <= c <= 'z':
            result += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            result += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += c
    return result

LEVEL_UP = "XSHAZZ"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

async def SEndPacKeT(ChaT, OnLinE, TypE, PacKeT):
    if TypE == 'ChaT' and ChaT:
        ChaT.write(PacKeT)
        await ChaT.drain()
    elif TypE == 'OnLine' and OnLinE:
        OnLinE.write(PacKeT)
        await OnLinE.drain()

async def GeNeRaTeAccEss(uid, password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": await Ua(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"
    }
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=data, timeout=30, ssl=False) as response:
                if response.status == 200:
                    resp_data = await response.json()
                    open_id = resp_data.get("open_id")
                    access_token = resp_data.get("access_token")
                    if open_id and access_token:
                        return open_id, access_token
                    else:
                        print(f"[ERROR] No open_id/token in response: {resp_data}")
                        return None, None
                else:
                    resp_text = await response.text()
                    print(f"[ERROR] Auth failed with status {response.status}: {resp_text}")
                    return None, None
    except Exception as e:
        print(f"[ERROR] Auth request failed: {e}")
        return None, None

online_writer = None
whisper_writer = None
login_url, ob, version = AuToUpDaTE()
print(f"\n[DEBUG] Login URL: {login_url}")
print(f"[DEBUG] Version: {version}\n")
Hr = {
    'User-Agent': Uaa(),
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': ob
}
CURRENT_BOT_UID = None
region = 'IN'

async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = version
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWAUOUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return await encrypted_proto(string)

async def MajorLogin(payload):
    url = f"{login_url}MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    try:
        # Try the standard endpoint
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=payload, headers=Hr, ssl=ssl_context, timeout=30) as response:
                if response.status == 200:
                    data = await response.read()
                    if data and len(data) > 0:
                        return data
                    else:
                        print(f"[ERROR] MajorLogin returned empty response")
                        return None
                elif response.status == 404:
                    # Try alternate endpoint format
                    print(f"[WARNING] MajorLogin 404 at {url}, trying alternate format...")
                    alt_url = f"{login_url.rstrip('/')}/login/oauth/token"
                    print(f"[DEBUG] Trying alternate URL: {alt_url}")
                    try:
                        async with session.post(alt_url, data=payload, headers=Hr, ssl=ssl_context, timeout=30) as alt_response:
                            if alt_response.status == 200:
                                data = await alt_response.read()
                                if data and len(data) > 0:
                                    return data
                    except:
                        pass
                    print(f"[ERROR] MajorLogin returned status {response.status}")
                    return None
                else:
                    print(f"[ERROR] MajorLogin returned status {response.status}")
                    return None
    except Exception as e:
        print(f"[ERROR] MajorLogin exception: {e}")
        return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization'] = f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200:
                return await response.read()
            return None

async def DecRypTMajoRLoGin(data):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(data)
    return proto

async def DecRypTLoGinDaTa(data):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(data)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto

async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9:
        headers = '0000000'
    elif uid_length == 8:
        headers = '00000000'
    elif uid_length == 10:
        headers = '000000'
    elif uid_length == 7:
        headers = '000000000'
    else:
        headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"

async def join_teamcode_packet(team_code, key, iv, region):
    fields = {
        1: 4,
        2: {
            4: bytes.fromhex("01090a0b121920"),
            5: str(team_code),
            6: 6,
            8: 1,
            9: {2: 800, 6: 11, 8: "1.111.1", 9: 5, 10: 1}
        }
    }
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def start_auto_packet(key, iv, region):
    fields = {1: 9, 2: {1: 12480598706}}
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def leave_squad_packet(key, iv, region):
    fields = {1: 7, 2: {1: 12480598706}}
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def heartbeat_packet(key, iv, region):
    """Generate heartbeat/keepalive packet to maintain online presence"""
    fields = {1: 2}  # Heartbeat type
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

auto_start_running = False
stop_auto = False
auto_start_task = None
start_spam_duration = 18
wait_after_match = 5
start_spam_delay = 0.1

# Multi-bot configuration
TOTAL_BOTS = 4
active_bots = {}
bots_lock = asyncio.Lock()
shared_team_code = None
shared_auto_running = False

async def auto_start_loop_multi_bot(bot_id, team_code, uid, chat_id, chat_type, key, iv, region, online_writer_ref, whisper_writer_ref):
    """Auto-start loop for individual bot with continuous restart after matches"""
    global stop_auto
    restart_count = 0
    while not stop_auto:
        try:
            join_pkt = await join_teamcode_packet(team_code, key, iv, region)
            if online_writer_ref['writer']:
                online_writer_ref['writer'].write(join_pkt)
                await online_writer_ref['writer'].drain()
            print(f"[BOT{bot_id}] Joined squad with team code: {team_code}")
            await asyncio.sleep(2)

            start_pkt = await start_auto_packet(key, iv, region)
            end_time = time.time() + start_spam_duration
            while time.time() < end_time and not stop_auto:
                if online_writer_ref['writer']:
                    online_writer_ref['writer'].write(start_pkt)
                    await online_writer_ref['writer'].drain()
                await asyncio.sleep(start_spam_delay)
            
            print(f"[BOT{bot_id}] Auto-start spam finished")

            if stop_auto:
                break

            waited = 0
            while waited < wait_after_match and not stop_auto:
                await asyncio.sleep(1)
                waited += 1
            
            if stop_auto:
                break

            leave_pkt = await leave_squad_packet(key, iv, region)
            if online_writer_ref['writer']:
                online_writer_ref['writer'].write(leave_pkt)
                await online_writer_ref['writer'].drain()
            print(f"[BOT{bot_id}] Left squad")
            await asyncio.sleep(2)
            
            restart_count += 1
            print(f"[BOT{bot_id}] ✅ Match cycle {restart_count} completed. Restarting in 3 seconds...")
            await asyncio.sleep(3)

        except Exception as e:
            print(f"[BOT{bot_id}] ❌ Error: {e}")
            await asyncio.sleep(5)
    print(f"[BOT{bot_id}] 🛑 Stopped after {restart_count} cycles")

async def auto_start_loop(team_code, uid, chat_id, chat_type, key, iv, region):
    global auto_start_running, stop_auto
    while not stop_auto:
        try:
            join_pkt = await join_teamcode_packet(team_code, key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_pkt)
            await asyncio.sleep(2)

            start_pkt = await start_auto_packet(key, iv, region)
            end_time = time.time() + start_spam_duration
            while time.time() < end_time and not stop_auto:
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', start_pkt)
                await asyncio.sleep(start_spam_delay)

            if stop_auto:
                break

            waited = 0
            while waited < wait_after_match and not stop_auto:
                await asyncio.sleep(1)
                waited += 1
            if stop_auto:
                break

            leave_pkt = await leave_squad_packet(key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_pkt)
            await asyncio.sleep(2)

        except Exception as e:
            print(f"[AUTO] Error: {e}")
            break
    auto_start_running = False
    stop_auto = False

async def stop_auto_loop():
    global auto_start_running, stop_auto, auto_start_task
    stop_auto = True
    if auto_start_task and not auto_start_task.done():
        auto_start_task.cancel()
        try:
            await auto_start_task
        except asyncio.CancelledError:
            pass
    auto_start_running = False

async def safe_send_message(chat_type, message, target_uid, chat_id, key, iv, max_retries=3):
    for attempt in range(max_retries):
        try:
            P = await SEndMsG(chat_type, message, target_uid, chat_id, key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
            return True
        except Exception:
            if attempt < max_retries - 1:
                await asyncio.sleep(0.5)
    return False

async def TcPOnLine(ip, port, jwt_token, bot_uid, key, iv, AutHToKen, online_writer_ref, reconnect_delay=0.5, bot_id=1, region='IN'):
    heartbeat_interval = 5  # Send heartbeat every 5 seconds
    while True:
        try:
            reader, writer = await asyncio.open_connection(ip, int(port))
            online_writer_ref['writer'] = writer
            writer.write(bytes.fromhex(AutHToKen))
            await writer.drain()
            print(f"[BOT{bot_id}] 🟢 Online connection established (IP: {ip}:{port})")
            
            last_heartbeat = time.time()
            
            while True:
                # Send periodic heartbeat to maintain online presence
                if time.time() - last_heartbeat >= heartbeat_interval:
                    try:
                        hb_pkt = await heartbeat_packet(key, iv, region)
                        if online_writer_ref['writer']:
                            online_writer_ref['writer'].write(hb_pkt)
                            await online_writer_ref['writer'].drain()
                        last_heartbeat = time.time()
                    except Exception as hb_err:
                        print(f"[BOT{bot_id}] Heartbeat error: {hb_err}")
                        break
                
                # Try to read server responses (non-blocking)
                try:
                    data = await asyncio.wait_for(reader.read(9999), timeout=1.0)
                    if not data:
                        print(f"[BOT{bot_id}] 🔴 Online connection closed by server")
                        break
                except asyncio.TimeoutError:
                    # No data, continue (heartbeat will be sent next iteration)
                    continue
                    
            writer.close()
            await writer.wait_closed()
            online_writer_ref['writer'] = None
        except Exception as e:
            print(f"[BOT{bot_id}] 🔴 Online error: {e}")
            if online_writer_ref['writer']:
                try:
                    online_writer_ref['writer'].close()
                    await online_writer_ref['writer'].wait_closed()
                except:
                    pass
                online_writer_ref['writer'] = None
        print(f"[BOT{bot_id}] 🔄 Reconnecting to online server in {reconnect_delay}s...")
        await asyncio.sleep(reconnect_delay)

async def TcPChaT(bot_id, ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region, online_writer_ref, reconnect_delay=0.5):
    global stop_auto
    whisper_writer_ref = {'writer': None}
    while True:
        try:
            reader, writer = await asyncio.open_connection(ip, int(port))
            whisper_writer_ref['writer'] = writer
            writer.write(bytes.fromhex(AutHToKen))
            await writer.drain()
            ready_event.set()

            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                pK = await AuthClan(clan_id, clan_compiled_data, key, iv)
                if whisper_writer_ref['writer']:
                    writer.write(pK)
                    await writer.drain()

            while True:
                data = await reader.read(9999)
                if not data:
                    break

                if data.hex().startswith("120000"):
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        inPuTMsG = response.Data.msg.strip().lower()
                        print(f"[BOT{bot_id}] Msg: {inPuTMsG} from {uid}")

                        if inPuTMsG.startswith('/lw '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                await safe_send_message(response.Data.chat_type, "[B][C][FF0000]Usage: /lw <team_code>", uid, chat_id, key, iv)
                                continue
                            team_code = parts[1]
                            if not team_code.isdigit():
                                await safe_send_message(response.Data.chat_type, "[B][C][FF0000]Team code must be numbers", uid, chat_id, key, iv)
                                continue
                            
                            await safe_send_message(response.Data.chat_type, f"[B][C][00FF00]🤖 All 4 Bots starting auto squad for team {team_code}\nUse /stop_auto to stop all bots", uid, chat_id, key, iv)
                            await start_all_bots(team_code, uid, chat_id, response.Data.chat_type, key, iv, region, online_writer_ref, whisper_writer_ref)

                        elif inPuTMsG.strip() == '/stop_auto':
                            await stop_all_bots()
                            await safe_send_message(response.Data.chat_type, "[B][C][00FF00]✅ All bots stopped", uid, chat_id, key, iv)

                        elif inPuTMsG.strip() in ('/help', 'help', '/menu', 'menu'):
                            help_msg = (
                                "[B][C][00FF00]━━━━━━━━━━\n"
                                "     🤖 MULTI-BOT COMMANDS\n"
                                "━━━━━━━━━━\n"
                                "[FFFFFF]/lw <team_code>  [00FF00]- Start all 4 bots\n"
                                "[FFFFFF]/stop_auto       [00FF00]- Stop all bots\n"
                                "[FFFFFF]/help            [00FF00]- Show this menu\n"
                                "━━━━━━━━━━\n"
                                f"[00FF00]Bots Running: {TOTAL_BOTS}\n"
                                f"[00FF00]Developer : {LEVEL_UP}\n"
                            )
                            await safe_send_message(response.Data.chat_type, help_msg, uid, chat_id, key, iv)

                    except Exception as e:
                        print(f"[BOT{bot_id}] Decode error: {e}")

            whisper_writer_ref['writer'].close()
            await whisper_writer_ref['writer'].wait_closed()
            whisper_writer_ref['writer'] = None
        except Exception as e:
            print(f"[BOT{bot_id}] Chat error: {e}")
            if whisper_writer_ref['writer']:
                try:
                    whisper_writer_ref['writer'].close()
                    await whisper_writer_ref['writer'].wait_closed()
                except:
                    pass
                whisper_writer_ref['writer'] = None
        await asyncio.sleep(reconnect_delay)

async def start_all_bots(team_code, uid, chat_id, chat_type, key, iv, region, online_writer_ref, whisper_writer_ref):
    """Start auto-start loop for all 4 bots"""
    global stop_auto, active_bots
    stop_auto = False
    
    async with bots_lock:
        # Create tasks for each bot
        for bot_id in range(1, TOTAL_BOTS + 1):
            if bot_id not in active_bots:
                task = asyncio.create_task(
                    auto_start_loop_multi_bot(bot_id, team_code, uid, chat_id, chat_type, key, iv, region, online_writer_ref, whisper_writer_ref)
                )
                active_bots[bot_id] = task
                print(f"[BOT{bot_id}] 🚀 Started")

async def stop_all_bots():
    """Stop all bot tasks"""
    global stop_auto, active_bots
    stop_auto = True
    
    async with bots_lock:
        for bot_id, task in active_bots.items():
            if task and not task.done():
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass
        active_bots.clear()

async def InitializeBot(bot_id, uid, password):
    """Initialize a single bot and connect to servers"""
    try:
        print(f"[BOT{bot_id}] 🔐 Logging in with UID: {uid}")

        open_id, access_token = await GeNeRaTeAccEss(uid, password)
        if not open_id:
            print(f"[BOT{bot_id}] ❌ Failed to get open_id/access_token - Invalid credentials?")
            return None

        print(f"[BOT{bot_id}] ✅ Got access token, authenticating...")
        print(f"[BOT{bot_id}] [DEBUG] Using login_url: {login_url}")
        payload = await EncRypTMajoRLoGin(open_id, access_token)
        login_resp = await MajorLogin(payload)
        if not login_resp:
            print(f"[BOT{bot_id}] ❌ MajorLogin failed - Server rejected authentication")
            print(f"[BOT{bot_id}] ℹ️  Check if UID/Password are correct or account is banned")
            print(f"[BOT{bot_id}] [DEBUG] Make sure you're using Garena account UID (not guest account)")
            return None
        
        print(f"[BOT{bot_id}] ✅ Authentication successful")
        auth = await DecRypTMajoRLoGin(login_resp)
        token = auth.token
        if not token:
            print(f"[BOT{bot_id}] ❌ No token in response")
            return None

        url = auth.url
        region = getattr(auth, 'region', 'IND')
        bot_uid = auth.account_uid
        key = auth.key
        iv = auth.iv
        timestamp = auth.timestamp

        print(f"[BOT{bot_id}] 📡 Connecting to game servers...")
        login_data = await GetLoginData(url, payload, token)
        if not login_data:
            print(f"[BOT{bot_id}] ❌ GetLoginData failed")
            return None
        ports = await DecRypTLoGinDaTa(login_data)
        online_ip, online_port = ports.Online_IP_Port.split(":")
        chat_ip, chat_port = ports.AccountIP_Port.split(":")

        auth_token = await xAuThSTarTuP(int(bot_uid), token, int(timestamp), key, iv)

        print(f"[BOT{bot_id}] ✅ Initialization complete - Ready to connect")
        return {
            'bot_id': bot_id,
            'uid': uid,
            'chat_ip': chat_ip,
            'chat_port': chat_port,
            'online_ip': online_ip,
            'online_port': online_port,
            'auth_token': auth_token,
            'key': key,
            'iv': iv,
            'ports': ports,
            'region': region
        }
    except Exception as e:
        print(f"[BOT{bot_id}] ❌ Initialization error: {e}")
        traceback.print_exc()
        return None

async def MaiiiinE():
    global CURRENT_BOT_UID, region
    if not os.path.exists("bot.txt"):
        print("❌ bot.txt not found. Create it with multiple bots:")
        print('{"UID1": "PASSWORD1", "UID2": "PASSWORD2", "UID3": "PASSWORD3", "UID4": "PASSWORD4"}')
        return None
    with open("bot.txt", "r") as f:
        creds = json.load(f)
    if not creds:
        print("❌ bot.txt is empty or invalid JSON")
        return None
    
    # Get only the first TOTAL_BOTS credentials
    cred_items = list(creds.items())[:TOTAL_BOTS]
    
    if len(cred_items) < TOTAL_BOTS:
        print(f"⚠️  Warning: Only {len(cred_items)} bots found, need {TOTAL_BOTS}")
    
    print(f"🚀 Starting {len(cred_items)} bots...")
    
    # Initialize all bots
    bot_tasks = []
    for idx, (uid, password) in enumerate(cred_items, 1):
        bot_data = await InitializeBot(idx, uid, password)
        if bot_data:
            # Create connection tasks for this bot
            online_writer_ref = {'writer': None}
            ready = asyncio.Event()
            
            task1 = asyncio.create_task(
                TcPChaT(idx, bot_data['chat_ip'], bot_data['chat_port'], 
                       bot_data['auth_token'], bot_data['key'], bot_data['iv'], 
                       bot_data['ports'], ready, bot_data['region'], 
                       online_writer_ref)
            )
            task2 = asyncio.create_task(
                TcPOnLine(bot_data['online_ip'], bot_data['online_port'], 
                         bot_data['auth_token'], bot_data['uid'], 
                         bot_data['key'], bot_data['iv'], 
                         bot_data['auth_token'], online_writer_ref, 
                         bot_id=idx, region=bot_data['region'])
            )
            bot_tasks.extend([task1, task2])
            print(f"[BOT{idx}] ✅ Online - Ready for commands")
        else:
            print(f"[BOT{idx}] Failed to initialize")
        await asyncio.sleep(2)  # Stagger the logins
    
    if bot_tasks:
        print(f"✅ All {len(cred_items)} bots ready! Use /lw <team_code> to start")
        await asyncio.gather(*bot_tasks)
    else:
        print("❌ No bots were initialized successfully")
        return None

async def StarTinG():
    while True:
        try:
            await MaiiiinE()
        except Exception as e:
            print(f"Restarting due to error: {e}")
            traceback.print_exc()
            await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.run(StarTinG())