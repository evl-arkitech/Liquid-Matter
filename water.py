import sys
import os
import urllib.request
import json

def print_water_logo():
    print(r"""
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
    if len(sys.argv) < 3 or sys.argv[1] != "install":
        print("Usage: python water.py install <package_name>")
    else:
        install_package(sys.argv[2])
