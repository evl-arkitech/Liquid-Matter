import sys
import os
import urllib.request
import json

def print_water_logo():
    print(r"""
 __          __  _______  ______  _____  
 \ \        / / |__   __||  ____||  __ \ 
  \ \  /\  / /     | |   | |__   | |__) |
   \ \/  \/ /      | |   |  __|  |  _  / 
    \  /\  /       | |   | |____ | | \ \ 
     \/  \/        |_|   |______||_|  \_\
                                         
    Liquid Matter Package Manager v1.0
    """)

def install_package(package_name):
    print(f"[*] Searching for '{package_name}' in the WATER registry...")
    # Simulate a registry fetch
    modules_dir = os.path.join(os.getcwd(), 'modules')
    if not os.path.exists(modules_dir):
        os.makedirs(modules_dir)
        
    pkg_path = os.path.join(modules_dir, f"{package_name}.lm")
    
    # In a real environment, this would fetch from a central DB or GitHub.
    # We will simulate downloading a standard library package.
    mock_code = f'display "Loaded module: {package_name}"\n'
    
    with open(pkg_path, 'w') as f:
        f.write(mock_code)
        
    print(f"[SUCCESS] Successfully poured '{package_name}' into ./modules/{package_name}.lm")

if __name__ == "__main__":
    print_water_logo()
    if len(sys.argv) < 3 or sys.argv[1] != "install":
        print("Usage: python water.py install <package_name>")
    else:
        install_package(sys.argv[2])
