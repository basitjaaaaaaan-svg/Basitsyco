import os, sys, time, random, re
try:
    import requests
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    os.system('pip install requests selenium webdriver-manager')
    print("Zaroori files install ho rahi hain... Tool restart karein.")
    sys.exit()

# --- Automatic Data Generator ---
eng_first = ["James", "Robert", "John", "Michael", "David", "William", "Richard", "Joseph", "Thomas", "Charles"]
eng_last = ["Smith", "Brown", "Wilson", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin"]

def generate_temp_email():
    """Tool khud se naya email banaye ga"""
    random_user = "".join(random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=8))
    domains = ["@mail7.io", "@chapsmail.com", "@instaddr.win", "@vintomaper.com"]
    return random_user + random.choice(domains)

def start_master_reg():
    os.system('clear')
    print("\033[1;92m--- BASIT SYCO AUTO-REG (TEMP-MAIL MODE) ---")
    print("\033[1;37mStatus: Full Automatic English IDs")
    print("-------------------------------------------")
    
    try:
        count = int(input("[+] Kitni IDs banani hain?: "))
        fixed_pass = input("[+] Password jo har ID par lagay: ")
        
        # Selenium Setup for PC
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        print("\n\033[1;94m[!] Chrome khul raha hai... Tayyar rahain.")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        for i in range(count):
            f_name = random.choice(eng_first)
            l_name = random.choice(eng_last)
            email = generate_temp_email() # Automatic Email
            
            print(f"\n\033[1;32m[{i+1}] Making ID for: {f_name} {l_name}")
            print(f"\033[1;37mEmail Used: {email}")
            
            driver.get("https://m.facebook.com/reg/")
            time.sleep(random.randint(4, 7))
            
            try:
                # Filling Details
                driver.find_element(By.NAME, "firstname").send_keys(f_name)
                driver.find_element(By.NAME, "lastname").send_keys(l_name)
                driver.find_element(By.NAME, "reg_email__").send_keys(email)
                driver.find_element(By.NAME, "reg_passwd__").send_keys(fixed_pass)
                
                # DOB
                driver.find_element(By.ID, "day").send_keys(str(random.randint(1,28)))
                driver.find_element(By.ID, "month").send_keys(str(random.randint(1,12)))
                driver.find_element(By.ID, "year").send_keys(str(random.randint(1992, 2004)))
                
                print("\033[1;33m[!] Form bhar diya gaya hai. Signup par click karein.")
                print("\033[1;37mAgar OTP maangay to Temp-mail site check karein.")
                
                # Save data for record
                with open('created_ids.txt', 'a') as f:
                    f.write(f"Name: {f_name} {l_name} | Email: {email} | Pass: {fixed_pass}\n")
                
                # Wait for you to see what happened
                time.sleep(20) 
                
            except Exception as e:
                print(f"\033[1;31m[!] Error: {e}")
                
        driver.quit()
        print("\n\033[1;92mSaara kaam khatam ho gaya!")
        
    except Exception as e:
        print(f"\033[1;31m[!] Galti: {e}")

def menu():
    os.system('clear')
    print("\033[1;32m  ____                _ _   ")
    print(" | __ )  __ _ ___(_) |_ ")
    print(" |  _ \ / _` / __| | __|")
    print(" | |_) | (_| \__ \ | |_ ")
    print(" |____/ \__,_|___/_|\__| Master Tool")
    print("\n\033[1;37m[1] Start Auto Creation (PC - Selenium)")
    print("[2] Update Tool (Git Pull)")
    print("[0] Exit")
    
    choice = input("\nSelect: ")
    if choice == '1': start_master_reg()
    elif choice == '2': 
        os.system('git pull')
        print("Updated!"); time.sleep(1); os.system('python basitsyco.py')
    else: sys.exit()

if __name__ == "__main__":
    menu()
