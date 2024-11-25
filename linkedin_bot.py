from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--detach")
chrome_options.add_argument("--ignore-certificate-errors") 
import time 

driver = webdriver.Chrome(options=chrome_options)
def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()
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
                



   
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    email_input.clear()
    email_input.send_keys("xxxxxxxxxxxxxx@gmail.com")

    
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_input.clear()
    password_input.send_keys("xxxxxxxxxx")

    
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign in')]"))
    )
    sign_in_button.click()
    print("Successfully signed in.")

    # Navigate to the Jobs section
    jobs_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='global-nav']/div/nav/ul/li[3]/a/div/div/li-icon/svg"))
    )
    jobs_icon.click()
    print("Jobs section opened.")


    time.sleep(5)

    all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

    # Apply for Jobs
    for listing in all_listings:
        print("Opening Listing")
        listing.click()
        time.sleep(2)
        try:
            # Click Apply Button
            apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
            apply_button.click()

            # Insert Phone Number
            # Find an <input> element where the id contains phoneNumber
            time.sleep(5)
            phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
            if phone.text == "":
                phone.send_keys("930xxxxx310")

            # Check the Submit Button
            submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
            if submit_button.get_attribute("data-control-name") == "continue_unify":
                abort_application()
                print("Complex application, skipped.")
                continue
            else:
                # Click Submit Button
                print("Submitting job application")
                submit_button.click()

            time.sleep(2)
            # Click Close Button
            close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
            close_button.click()

        except NoSuchElementException:
            abort_application()
            print("No application button, skipped.")
            continue

        time.sleep(5)
        driver.quit()


finally:
    input("Press Enter to exit...")
    driver.quit()
