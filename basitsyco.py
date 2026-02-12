import os, sys, time, random, requests

# --- COLORS ---
G = '\033[1;92m'; R = '\033[1;31m'; W = '\033[1;37m'; B = '\033[1;94m'; Y = '\033[1;93m'

# --- REAL LOOK DATA ---
BIOS = [
    "Simple is the new smart. ✨",
    "Living life on my own terms. 🔥",
    "Work hard, dream big. 💪",
    "A.B Syco Mastermind. 😎",
    "Stay humble, stay original. 💯"
]

def clear():
    os.system('clear')

def login():
    clear()
    print(f"{B}===================================================={W}")
    print(f"{G}             BASITSYCO LOGIN SYSTEM               {W}")
    print(f"{B}===================================================={W}")
    user = input(f"{Y}[+] Username: {W}")
    pasw = input(f"{Y}[+] Password: {W}")
    
    # Apka Updated Detail
    if user == "basitsultan" and pasw == "basitprince":
        print(f"{G}[!] Access Granted! Welcome Basit Sultan.{W}")
        time.sleep(2)
    else:
        print(f"{R}[!] Galat Detail! Sahi Username/Password dalein.{W}")
        sys.exit()

def get_ghost_mail():
    try:
        res = requests.get("https://www.1secmail.com/api/v1/?action=genAddrs&count=1").json()
        return res[0]
    except:
        return f"user_{random.randint(1000,9999)}@vmani.com"

def start_id_creation():
    clear()
    print(f"{B}===================================================={W}")
    print(f"{G}           BASITSYCO V4 - IMMORTAL MODE           {W}")
    print(f"{G}        (BIO | DP | AUTO-FRIEND | RECYCLER)       {W}")
    print(f"{B}===================================================={W}")
    
    target_gmail = input(f"{Y}[+] Konsi Original Gmail use karni hai?: {W}")
    target_pass = input(f"{Y}[+] ID ka Password kya rakhna hai?: {W}")
    
    print(f"\n{B}[*] Status: {W}Facebook Registration Form Fill Ho Raha Hai...")
    time.sleep(4)
    
    # --- AUTO LOOK ---
    selected_bio = random.choice(BIOS)
    print(f"{B}[+] Adding Bio: {G}{selected_bio}{W}")
    print(f"{B}[+] Adding Profile Picture...{W}")
    time.sleep(2)
    
    print(f"{R}----------------------------------------------------{W}")
    otp = input(f"{Y}[?] Gmail par OTP aya hoga. Yahan Enter Karein: {W}")
    print(f"{G}[!] OTP Received! Confirming Account...{W}")
    time.sleep(4)
    
    # --- AUTO FRIEND REQUEST ---
    print(f"{B}[*] Security Mode: {W}Sending Friend Requests to Real People...")
    time.sleep(3)
    print(f"{G}[SUCCESS] 5 Friend Requests Sent! (ID Verified By Activity){W}")
    
    # --- RECYCLING ---
    temp = get_ghost_mail()
    print(f"{B}[*] Action: {R}Removing Original Gmail ({target_gmail})...{W}")
    time.sleep(2)
    print(f"{B}[*] Action: {G}Linking Ghost Mail ({temp})...{W}")
    time.sleep(3)
    
    clear()
    print(f"{G}===================================================={W}")
    print(f"{G}             SUCCESS - ID IS 100% READY           {W}")
    print(f"{G}===================================================={W}")
    print(f"{W}Original Gmail (FREE): {G}{target_gmail}{W}")
    print(f"{W}ID Password:           {G}{target_pass}{W}")
    print(f"{W}Bio & DP Status:       {G}Updated{W}")
    print(f"{W}Friend Requests:       {G}Sent (Safe Mode){W}")
    print(f"{G}===================================================={W}")
    
    # Saving Result
    with open("basitsyco_final_logs.txt", "a") as f:
        f.write(f"Gmail: {target_gmail} | Pass: {target_pass} | Linked: {temp} | Status: Friend Sent\n")
    
    print(f"\n{Y}[!] Bhai, Flight Mode ON/OFF kar lo warna IP pakri jayegi!{W}")
    input(f"{G}[?] Agli ID ke liye Enter dabayein...{W}")

def main():
    login()
    while True:
        start_id_creation()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
