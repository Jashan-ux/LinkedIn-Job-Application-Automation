from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--detach")
chrome_options.add_argument("--ignore-certificate-errors") 


driver = webdriver.Chrome(options=chrome_options)

try:
    
    driver.get(
        "https://www.linkedin.com/jobs/search/?currentJobId=4077191677&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"
    )

    
    try:
        
        sign_in_modal_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign in')]"))
        )
        print("Interface 1: Modal detected.")
        sign_in_modal_button.click()

    except:
        try:
            
            main_sign_in_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
            )
            print("Interface 2: Main page detected.")
            main_sign_in_button.click()

        except:
            try:
               
                email_input = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, "username"))
                )
                print("Interface 3: Direct login form detected.")
            except:
                print("No recognizable login interface detected.")
                driver.quit()
                exit()

   
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    email_input.clear()
    email_input.send_keys("Jash.100daysoxxxx@gmail.com")

    
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_input.clear()
    password_input.send_keys("xxxxxxxxx")

    
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign in')]"))
    )
    sign_in_button.click()
    print("Successfully signed in.")

    jobs_icon = driver.find_element(By.XPATH, "//*[@id='global-nav']/div/nav/ul/li[3]/a")
    jobs_icon.click()
    print("Jobs icon clicked.")

    
    easy_apply_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(@aria-label, 'Easy Apply')]"))
    )
    
    easy_apply_button.click()
    print("Easy Apply button clicked.")

    
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='phoneNumber']"))
    )
    phone_input.clear()
    phone_input.send_keys("930666231x")
    print("Phone number entered.")

    
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Next']"))
    )
    next_button.click()
    print("Next button clicked.")

finally:
    input("Press Enter to exit...")
    driver.quit()
