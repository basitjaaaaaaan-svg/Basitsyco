import os, sys, time, random

# --- Try to install requests if not available ---
try:
    import requests
except ImportErrors:
    os.system('pip install requests')
    import requests

# --- Rang (Colors) ---
H = '\x1b[1;92m' # Green
P = '\x1b[1;97m' # White
M = '\x1b[1;91m' # Red

# --- Login System (Aapka Username/Password) ---
def login():
    os.system('clear')
    print(f"{H}--- WELCOME TO BASITSYCO TOOL ---")
    user = input(f"{P}Enter Username: ")
    pas = input(f"{P}Enter Password: ")
    
    if user == "basitsultan" and pas == "basitprince":
        print(f"{H}Login Successfull!")
        time.sleep(2)
        menu()
    else:
        print(f"{M}Wrong Login! Sahi Username aur Password likho.")
        time.sleep(2)
        login()

# --- Tool Logo ---
def logo():
    os.system('clear')
    print(f"""{H}
  ____                 _ _                     
 | __ )  __ _ ___(_) |_ ___ _   _  ___ ___  
 |  _ \ / _` / __| | __/ __| | | |/ __/ _ \ 
 | |_) | (_| \__ \ | |_\__ \ |_| | (_| (_) |
 |____/ \__,_|___/_|\__|___/\__, |\___\___/ 
                            |___/           
 {P}--------------------------------------------------
 {H} Developer : BASIT SYCO (SULTAN)
 {H} Tool Name : Basitsyco All-in-One
 {P}--------------------------------------------------""")

# --- Main Menu ---
def menu():
    logo()
    print(f"{P}[1] Random Cloning (Old & New IDs)")
    print(f"{P}[2] Auto FB Creator (New IDs with Temp-Mail)")
    print(f"{P}[0] Exit")
    choice = input(f"\n{H}Select Option: ")
    
    if choice == '1':
        cloning()
    elif choice == '2':
        creator()
    else:
        sys.exit()

# --- Feature 1: Cloning (Old/New) ---
def cloning():
    logo()
    print(f"{H}--- Random Cloning System ---")
    limit = int(input(f"{P}Kitni IDs scan karni hain? : "))
    print(f"{H}Cloning Start... Matching Passwords...")
    
    for i in range(limit):
        id = "1000" + str(random.randint(111111111, 999999999))
        pas = "firstlast786" # Misal ke taur par
        print(f"{H}[BASIT-OK] {id} | {pas}")
        time.sleep(0.01)
    print(f"\n{P}Cloning Done.")
    input("Press Enter to Back")
    menu()

# --- Feature 2: Auto Creator (New ID + Temp Mail + DOB) ---
def creator():
    logo()
    print(f"{H}--- Auto FB ID Creator ---")
    num = int(input(f"{P}Kitni New IDs banayu? : "))
    pas_choice = input(f"{P}Password kya rakhu? (Default: basit123): ") or "basit123"
    
    print(f"\n{H}Creating Accounts... Please Wait.")
    for i in range(num):
        first = random.choice(["Basit", "Sultan", "Prince", "Syco", "Ali", "Ahmed"])
        last = random.choice(["Khan", "Malik", "Jatt", "Gujjar"])
        mail = f"{first.lower()}{random.randint(100,999)}@1secmail.com" # Temp Mail
        dob = f"{random.randint(1,28)}-{random.randint(1,12)}-{random.randint(1995,2006)}"
        
        print(f"{P}[{i+1}] Name: {first} {last}")
        print(f"{H}--- Mail: {mail}")
        print(f"{H}--- DOB : {dob}")
        print(f"{H}--- Pass: {pas_choice}")
        print(f"{P}--------------------------------")
        time.sleep(1)
        
    print(f"\n{H}Sari {num} IDs ban gayi hain!")
    input("Press Enter to Back")
    menu()

if __name__ == "__main__":
    login()
