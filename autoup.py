import requests
import urllib3
from google_play_scraper import app

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def AuToUpDaTE():
    try:
        result = app('com.dts.freefireth', lang="fr", country='fr')
        version = result['version']
    except Exception as e:
        print(f"[WARNING] Failed to get version from Play Store: {e}")
        version = "1.123.1"  # Fallback version
    
    try:
        r = requests.get(
            f'https://bdversion.ggbluefox.com/live/ver.php?version={version}&lang=ar&device=android&channel=android&appstore=googleplay&region=ME&whitelist_version=1.3.0&whitelist_sp_version=1.0.0&device_name=google%20G011A&device_CPU=ARMv7%20VFPv3%20NEON%20VMH&device_GPU=Adreno%20(TM)%20640&device_mem=1993',
            verify=False,
            timeout=10
        )
        
        if r.status_code == 200:
            data = r.json()
            url = data.get('server_url', 'https://100067.connect.garena.com/')
            ob = data.get('latest_release_version', version)
        else:
            print(f"[WARNING] Version server returned status {r.status_code}, using fallback")
            url = 'https://100067.connect.garena.com/'
            ob = version
    except Exception as e:
        print(f"[WARNING] Version check failed: {e}, using fallback")
        url = 'https://100067.connect.garena.com/'
        ob = version
    
    return url, ob, version