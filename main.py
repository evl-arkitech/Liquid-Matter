import sys
import winsound
from lexer import Lexer
from parser import Parser
from evaluator import Evaluator

def print_license():
    logo = r"""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄     ▄▄▄  ▄▄▄
▐░░░░░░░░░░░▌▐░░░▌   ▐░░░▌▐░░░▌
▐░█▀▀▀▀▀▀▀▀▀  ▀░░▌   ▐░░▀ ▐░░░▌
▐░▌            ▀░░▌ ▐░░▀  ▐░░░▌
▐░█▄▄▄▄▄▄▄▄▄    ▀░░▐░░▀   ▐░░░▌
▐░░░░░░░░░░░▌    ▀░░░▀    ▐░░░▌
▐░█▀▀▀▀▀▀▀▀▀      ▀░▀     ▐░░░▌
▐░▌                ▀      ▐░░░▌
▐░█▄▄▄▄▄▄▄▄▄              ▐░░░▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌             ▐░░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀               ▀▀▀▀▀▀▀▀▀▀▀▀ 

 ▒▓████████▓▒░ Liquid Matter Engine v2.0 ░▒▓████████▓▒
 
 [!!] Governed by the EVL Public License (EPL v1.0)
 [!!] 1% Commercial Royalty Enforced.
"""
    try:
        print(logo)
    except UnicodeEncodeError:
        print(logo.encode('utf-8').decode('cp1252', 'ignore'))


def play_water_sound():
    try:
        # A sequence of rapid beeps increasing in frequency mimics a "drip" or "bloop"
        for freq in range(600, 1400, 150):
            winsound.Beep(freq, 30)
    except:
        pass

def run(code, evaluator):
    try:
        lexer = Lexer(code)
        parser = Parser(lexer)
        ast = parser.parse()
        evaluator.evaluate(ast)
    except Exception as e:
        play_water_sound()
        print(f"[*] [LIQUID ERROR] {e}")

def repl(env=None):
    if env is None:
        evaluator = Evaluator()
    else:
        evaluator = Evaluator(env)
    
    print("💧 Liquid Matter REPL v0.1 💧")
    print("Type a natural sentence (e.g. 'set age to 25') or 'exit' to quit.")
    while True:
        try:
            text = input('liquid> ')
        except EOFError:
            break
        if not text:
            continue
        if text.lower() == 'exit':
            break
        
        run(text, evaluator)

def run_file(filepath):
    try:
        import os
        with open(filepath, 'r') as f:
            code = f.read()
        evaluator = Evaluator()
        evaluator.loaded_modules.add(os.path.abspath(filepath))
        try:
            run(code, evaluator)
        except Exception as e:
            print(f"\n[FATAL ERROR] {e}")
            print("[WATER] Liquid Engine caught a fatal syntax crash!")
            print("[WATER] Dropping into interactive REPL mode so you don't lose your session...\n")
            repl(env=evaluator.env)
    except FileNotFoundError:
        print(f"[ERROR] Could not find file: {filepath}")

def print_help():
    help_text = """
    ======================================
    LIQUID MATTER - OFFICIAL CHEAT SHEET
    ======================================
    [CLI Commands]
    liquid run <file.lm>    Execute a script
    liquid repl             Open interactive shell
    liquid help             Show this menu
    python water.py install <pkg>  Download modules

    [Syntax Examples]
    Variables:   set x to 10
                 add 5 to x
                 subtract 2 from x
    Logic:       if x is 15 then ... end
    Loops:       repeat 5 times ... end
    Async:       async perform myAction
    Error:       attempt ... recover ... end
    JSON:        parse json data into list
                 get "key" from obj into val
                 for each item in list perform action
    Secrets:     load secrets
                 get secret "API_KEY" into key
    SQL:         query "SELECT * FROM users"
    Engine:      spawn Player at 0 0
                 when Player touches Enemy perform takeDamage
    """
    print(help_text)

def install_system():
    import os
    import shutil
    import winreg
    
    print("[*] Initiating Liquid Matter System Installation...")
    install_dir = r"C:\LiquidMatter"
    
    if not os.path.exists(install_dir):
        os.makedirs(install_dir)
        print(f"[+] Created directory: {install_dir}")
        
    exe_path = sys.executable
    target_path = os.path.join(install_dir, "liquid.exe")
    
    try:
        shutil.copy(exe_path, target_path)
        print(f"[+] Copied core engine to: {target_path}")
    except Exception as e:
        print(f"[!] Failed to copy executable: {e}")
        return
        
    print("[*] Injecting into Windows Global PATH...")
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_ALL_ACCESS)
        path_value, _ = winreg.QueryValueEx(key, "Path")
        if install_dir not in path_value:
            new_path = path_value + f";{install_dir}"
            winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
            print("[+] Successfully added to User PATH!")
        else:
            print("[-] Engine is already in the User PATH.")
        winreg.CloseKey(key)
    except Exception as e:
        print(f"[!] Failed to modify registry PATH: {e}")
        print("[!] Please run as Administrator or manually add C:\\LiquidMatter to your PATH.")
        return
        
    print("\n[SUCCESS] Liquid Matter is now permanently installed!")
    print("You may now open a NEW terminal anywhere and type: `liquid run script.lm`")

def main():
    print_license()
    if len(sys.argv) == 1 or sys.argv[1] == "repl":
        repl()
    elif sys.argv[1] in ["--help", "-h", "help"]:
        print_help()
    elif sys.argv[1] == "run":
        if len(sys.argv) < 3:
            print("[ERROR] Please specify a file to run. (e.g. 'liquid run script.lm')")
        else:
            run_file(sys.argv[2])
    elif sys.argv[1] == "install-system":
        install_system()
    elif sys.argv[1] in ["--version", "-v"]:
        print("Liquid Matter version 2.0.0 (Enterprise Release)")
    else:
        # Fallback to just running the file if passed directly
        run_file(sys.argv[1])

if __name__ == "__main__":
    main()
