from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://innovativeskillsltd.com/contact')

driver.maximize_window()

# name = "salman"

test_data = [
    ('Mujahid', 'mujahid', '123', '123', False),
    ('John', 'john@example.com', '123', '1234567890', False),
    ('John', 'john@', 'seccret123', '1234567890', False),
    ('John', 'john@example.com', 'seccret123', '1234567890', True),
]

for i, (name, email, password, phone, should_pass) in enumerate(test_data, start=1):
    print(f'\nRunning Test Case {i}...{name} {email}')

driver.find_element(By.NAME, "name").clear()
driver.find_element(By.NAME, "email").clear()

driver.find_element(By.NAME, "name").send_keys(name)
driver.find_element(By.NAME, "email").send_keys(email)

driver.find_element(By.TAG_NAME, 'form').submit()

time.sleep(20)
driver.quit()







