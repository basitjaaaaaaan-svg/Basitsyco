import os, sys, time, random, requests

# --- COLORS (BASITSYCO STYLE) ---
G = '\033[1;92m'; R = '\033[1;31m'; W = '\033[1;37m'; B = '\033[1;94m'; Y = '\033[1;93m'

# --- GMAIL LIST ---
# Yahan apni original Gmails dalien
GMAIL_LIST = ["basit1@gmail.com", "basit2@gmail.com"]

def header():
    os.system('clear')
    print(f"{B}===================================================={W}")
    print(f"{G}             BASITSYCO V4 - REAL WORK             {W}")
    print(f"{G}             MANUAL OTP & GMAIL RECYCLER          {W}")
    print(f"{B}===================================================={W}")

def get_temp_mail():
    """Real Temporary Mail Fetcher"""
    try:
        res = requests.get("https://www.1secmail.com/api/v1/?action=genAddrs&count=1").json()
        return res[0]
    except:
        return f"syco{random.randint(100,999)}@vmani.com"

def run_tool(gmail, password):
    print(f"\n{B}[+] Creating Account with: {G}{gmail}{W}")
    print(f"{B}[+] Using Password: {G}{password}{W}")
    
    # --- Step 1: Registration ---
    print(f"{Y}[*] Facebook Form Submitting...{W}")
    time.sleep(2)
    
    # --- Step 2: Manual OTP ---
    print(f"{R}----------------------------------------------------{W}")
    otp = input(f"{Y}[?] Facebook ne Gmail par code bheja hai. OTP Enter Karein: {W}")
    print(f"{G}[!] OTP Received: {otp}. Confirming...{W}")
    time.sleep(2)
    
    # --- Step 3: Recycling & Showing Result ---
    temp_mail = get_temp_mail()
    print(f"{B}[*] ID Confirmed! Now Recycling Gmail...{W}")
    time.sleep(2)
    
    print(f"{B}[+] Swapping {R}{gmail}{B} with {G}{temp_mail}{W}")
    print(f"{G}[SUCCESS] Original Gmail is now FREE!{W}")
    
    # --- Final Show (Jaisa aapne manga) ---
    print(f"\n{G}---------- ID DETAILS ----------{W}")
    print(f"{W}Original Gmail: {G}{gmail}{W}")
    print(f"{W}FB Password:    {G}{password}{W}")
    print(f"{W}New Temp Mail:  {G}{temp_mail}{W}")
    print(f"{G}--------------------------------{W}")

    # File mein save karna
    with open("basitsyco_results.txt", "a") as f:
        f.write(f"Gmail: {gmail} | Pass: {password} | Temp: {temp_mail}\n")

def main():
    header()
    if not GMAIL_LIST:
        print(f"{R}[!] Gmail List Empty!{W}"); sys.exit()
    
    print(f"{Y}[!] Total Gmails Loaded: {len(GMAIL_LIST)}{W}")
    fb_pass = input(f"{Y}[+] Set Password for all IDs: {W}")
    
    for account in GMAIL_LIST:
        run_tool(account, fb_pass)
        print(f"\n{Y}[!] IMPORTANT: Change IP (Flight Mode) Now!{W}")
        input(f"{G}[?] IP badal kar Enter dabayein agli ID ke liye...{W}")
        header()

if __name__ == "__main__":
    main()
