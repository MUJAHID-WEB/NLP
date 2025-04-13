from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set up Chrome options
chrome_options = Options()


##### 1. Use secondary Chrome profile in Users/mujahid folder -- creating new folder and copy all files and folder of main Chrome folder located at '/Users/mujahid/Library/Application Support/Google/Chrome' and delet all files and folder from profile-directory "Profile 2" .  it is the manual way to Create a custom profile directory 

# chrome_user_data = "/Users/mujahid/Library/Application Support/Google/Chrome"
# chrome_user_data = "/Users/mujahid/s_pro"
# chrome_options.add_argument(f"--user-data-dir={chrome_user_data}")
# chrome_options.add_argument("--profile-directory=Profile 2")

#### Create a custom profile directory to avoid conflicts by code 
custom_profile = os.path.expanduser("~/selenium_profile")
if not os.path.exists(custom_profile):
    os.makedirs(custom_profile)

chrome_options.add_argument(f"--user-data-dir={custom_profile}")
chrome_options.add_argument("--profile-directory=Default")  # Optional



#### Additional options
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--headless")  # Uncomment for headless mode


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

    # manually authenticate in this profile
print("Please manually log in to Google in this browser window...")
driver.get("https://accounts.google.com")
time.sleep(10)  


print("Accessing Google Form...")

driver.get('https://forms.gle/hBNo1ScjNsqkKbA1A')
print("Successfully loaded the form!")

driver.maximize_window()

time.sleep(5)

# 1. Name field
try:
    name_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
    )
    name_input.clear()
    name_input.send_keys("Mujahid")
    print("Successfully filled text field!")
except:
    print("Text input not found")

time.sleep(5)  

######### 2. Attendance radio button

# radio_btn_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'

response = "Yes,  I'll be there"
# response = "Sorry, can't make it"
# radio_btn_xpath = f'//div[@role="radio" and @aria-label="{response}"]'
radio_btn_xpath = f'//div[@data-value="{response}"]'

try:
    radio_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, radio_btn_xpath))
    )

    actions = ActionChains(driver)
    actions.move_to_element(radio_btn).click().perform()

    print("Radio Button clicked")

except: 
    print("Radio Button not clicked")

time.sleep(5)  

# 3. Date field
try:
    date_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='date']"))
    )
    date_input.send_keys("2025-04-15")
    print("Successfully filled date field!")

except: 
    print("Date field not filled")

time.sleep(5)

# 4. Food checkboxes
try:
    food_options = ["Mains", "Dessert"]  # Options: Mains, Salad, Dessert, Drinks, Sides/Appetizers
    for option in food_options:
        checkbox_xpath = f'//div[@role="checkbox" and @aria-label="{option}"]'

        checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, checkbox_xpath))
        )
        # driver.execute_script("arguments[0].click();", checkbox)
        actions = ActionChains(driver)
        actions.move_to_element(checkbox).click().perform()

        print(f"Selected food option: {option}")

except: 
    print("Food checkboxes not checked")

time.sleep(5)

# 5. Allergies dropdown
try:
    allergies = "No"  # Options: "Yes" or "No"
    dropdown_xpath = '//div[@role="listbox"]'
    option_xpath = f'//div[@role="option" and @data-value="{allergies}"]'
    
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, dropdown_xpath))
    )
    dropdown.click()
    time.sleep(1)
    
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, option_xpath))
    )
    option.click()
    print(f"Selected allergies option: {allergies}")

except: 
    print("Allergies dropdown not selected")

time.sleep(5)

# 6. File upload 

try:
    add_file_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and @aria-label='Add file']"))
    )
    add_file_btn.click()
    print("Clicked 'Add file' button")
    
    # Switch to the iframe 
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src, 'docs.google.com/picker')]"))
    )
    print("Switched to upload iframe")
    
    browse_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Browse']]"))
    )
    print("Found Browse button")

    file_input = driver.find_element(By.XPATH, "//input[@type='file']")
    
    file_path = "/Users/mujahid/Desktop/Resume of Mujahid.pdf"
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at: {file_path}")
    
    file_input.send_keys(file_path)
    print("File path sent to input")
    
    # Wait for upload to complete 
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, f"//div[contains(text(),'Resume of Mujahid.pdf')]"))
    )
    print("File uploaded successfully!")

    # Switch back to main content
    driver.switch_to.default_content()
    print("Switched back to main content")
    time.sleep(2)

 
    WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Resume of Mujahid.pdf')]"))
)

    print("File confirmed in form")
    
except: 
    print("File not uploaded")
    


####### Submit
# submit_btn_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
submit_btn_xpath = "//span[contains(text(),'Submit')]"

try:
    submit_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, submit_btn_xpath))
    )

    actions = ActionChains(driver)
    actions.move_to_element(submit_btn).click().perform()

    print("Submit Button clicked")

except: 
    print("Submit Button not clicked")

print("Keeping browser open for 5 seconds...")
time.sleep(5)  

driver.quit()
print("Browser closed")



