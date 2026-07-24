import sys
import os
import urllib.request
import json

if sys.platform == "win32":
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        if hasattr(sys.stderr, 'reconfigure'):
            sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

def safe_print(text=""):
    try:
        print(text)
    except UnicodeEncodeError:
        enc = getattr(sys.stdout, 'encoding', None) or 'utf-8'
        try:
            print(str(text).encode(enc, errors='replace').decode(enc, errors='replace'))
        except Exception:
            print(str(text).encode('ascii', errors='replace').decode('ascii'))

def print_water_logo():
    safe_print(r"""
 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▌
▐░█▀▀▀▀▀█░█▀▀▀▀▀█░█▀▀▀▀▀█░█▀▀▀▀▀▀▀▀▀█░█▀▀▀▀▀▀▀▀▀█░█▀▀▀▀█░▌
▐░▌     ▐░▌     ▐░▌     ▐░▌         ▐░▌         ▐░▌    ▐░▌
▐░▌  W  ▐░▌  A  ▐░▌  T  ▐░▌    E    ▐░▌    R    ▐░▌    ▐░▌
▐░▌     ▐░▌     ▐░▌     ▐░▌         ▐░▌         ▐░▌    ▐░▌
▐░█▄▄▄▄▄█░█▄▄▄▄▄█░█▄▄▄▄▄█░█▄▄▄▄▄▄▄▄▄█░█▄▄▄▄▄▄▄▄▄█░█▄▄▄▄█░▌
▐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

 ▒▓████████▓▒░ WATER GLOBAL REGISTRY v1.0 ░▒▓████████▓▒
 
 [~] Connecting to secure framework: evl-arkitech
""")

AUTH_FILE = os.path.join(os.getcwd(), "water.json")

def load_auth():
    if os.path.exists(AUTH_FILE):
        try:
            with open(AUTH_FILE, "r") as f:
                return json.load(f).get("uuid")
        except:
            return None
    return None

def set_auth(uuid):
    with open(AUTH_FILE, "w") as f:
        json.dump({"uuid": uuid}, f)
    print(f"[SUCCESS] Developer UUID securely bound to WATER Registry.")

def install_package(package_name):
    print(f"[*] Searching for '{package_name}' in the WATER registry...")
    
    modules_dir = os.path.join(os.getcwd(), 'modules')
    if not os.path.exists(modules_dir):
        os.makedirs(modules_dir)
        
    pkg_path = os.path.join(modules_dir, f"{package_name}.lm")
    
    # Fetch directly from the evl-arkitech public water-registry
    url = f"https://raw.githubusercontent.com/evl-arkitech/water-registry/main/packages/{package_name}.lm"
    
    
    try:
        req = urllib.request.Request(url)
        uuid = load_auth()
        if uuid:
            req.add_header('X-EVL-Auth', uuid)
            
        with urllib.request.urlopen(req) as response:
            code = response.read().decode('utf-8')
            
        with open(pkg_path, 'w', encoding='utf-8') as f:
            f.write(code)
            
        print(f"[SUCCESS] Successfully poured '{package_name}' into ./modules/{package_name}.lm")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"[ERROR] Package '{package_name}' does not exist in the WATER registry.")
        else:
            print(f"[ERROR] HTTP Error: {e.code}")
    except Exception as e:
        print(f"[ERROR] Failed to fetch package: {e}")

if __name__ == "__main__":
    print_water_logo()
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python water.py auth <uuid>")
        print("  python water.py install <package_name>")
    elif sys.argv[1] == "auth" and len(sys.argv) == 3:
        set_auth(sys.argv[2])
    elif sys.argv[1] == "install" and len(sys.argv) == 3:
        uuid = load_auth()
        if uuid:
            print(f"[AUTH] Authenticated as Developer ID: {uuid}")
        else:
            print("[WARN] Operating as an Anonymous Client. Use 'water auth <uuid>' to unlock publisher access.")
        install_package(sys.argv[2])
    else:
        print("Invalid Command.")
