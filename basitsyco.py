import os, sys, time, random, re
try:
    import requests
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    os.system('pip install requests selenium webdriver-manager')
    os.execl(sys.executable, sys.executable, *sys.argv)

# --- LOGIN SYSTEM (AS PER YOUR REQUEST) ---
def login():
    os.system('clear')
    print("\033[1;92m====================================")
    print("\033[1;93m      BASIT SYCO LOGIN SYSTEM")
    print("\033[1;92m====================================")
    user = input("\033[1;37m[+] Enter Username: ")
    pas = input("\033[1;37m[+] Enter Password: ")
    
    # Aapka bataya hua Username aur Password
    if user == "basitsultan" and pas == "basitprince":
        print("\033[1;92m\n[!] Login Successful! Access Granted.")
        time.sleep(2)
        menu()
    else:
        print("\033[1;31m\n[!] Wrong Details! Try again.")
        time.sleep(2)
        login()

# --- AUTO TEMP-MAIL GENERATOR ---
def generate_email():
    user = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8))
    num = random.randint(100, 999)
    domains = ["@mail7.io", "@chapsmail.com", "@vintomaper.com"]
    return f"{user}{num}{random.choice(domains)}"

# --- AUTOMATION PROCESS (PC ONLY) ---
def start_reg():
    os.system('clear')
    print("\033[1;92m--- FB AUTO-REG MASTER (PC ONLY) ---")
    try:
        count = int(input("\033[1;37m[+] How many IDs to create?: "))
        fixed_pass = input("[+] Fixed Password for IDs: ")
        
        print("\n\033[1;94m[!] Starting Chrome Browser on PC...")
        options = webdriver.ChromeOptions()
        # Browser security bypass aur real look ke liye
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        for i in range(count):
            f_name = random.choice(["James", "Robert", "John", "David", "William", "Richard", "Thomas"])
            l_name = random.choice(["Smith", "Brown", "Wilson", "Taylor", "Miller", "Davis", "Garcia"])
            email = generate_email()
            
            print(f"\n\033[1;32m[{i+1}] Processing: {f_name} {l_name}")
            print(f"\033[1;37mUsing Email: {email}")
            
            driver.get("https://m.facebook.com/reg/")
            time.sleep(random.randint(5, 8))
            
            # Filling Form
            driver.find_element(By.NAME, "firstname").send_keys(f_name)
            driver.find_element(By.NAME, "lastname").send_keys(l_name)
            driver.find_element(By.NAME, "reg_email__").send_keys(email)
            driver.find_element(By.NAME, "reg_passwd__").send_keys(fixed_pass)
            
            # DOB Selection
            driver.find_element(By.ID, "day").send_keys(str(random.randint(1, 28)))
            driver.find_element(By.ID, "month").send_keys(str(random.randint(1, 12)))
            driver.find_element(By.ID, "year").send_keys(str(random.randint(1995, 2005)))
            
            print("\033[1;33m[!] Details filled! Solve captcha or click 'Sign Up' if required.")
            
            # Record Save karna
            with open('created_ids.txt', 'a') as f:
                f.write(f"Name: {f_name} {l_name} | Email: {email} | Pass: {fixed_pass}\n")
            
            time.sleep(15) # Aapko browser dekhne ka time dena

        driver.quit()
        print("\n\033[1;92m[DONE] Process complete. Results saved in created_ids.txt")
    except Exception as e:
        print(f"\033[1;31m\n[!] Error: {e}")
        print("Note: Use PC with Chrome installed for this tool.")

def menu():
    os.system('clear')
    print("\033[1;32m   ____            _ _   ")
    print("  | __ )  __ _ ___(_) |_ ")
    print("  |  _ \ / _` / __| | __|")
    print("  | |_) | (_| \__ \ | |_ Master Tool")
    print("\n\033[1;37m[1] Start Auto Creation (PC Method)")
    print("[0] Exit")
    
    choice = input("\nSelect: ")
    if choice == '1': start_reg()
    else: sys.exit()

if __name__ == "__main__":
    login()
