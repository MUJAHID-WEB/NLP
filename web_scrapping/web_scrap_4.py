from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

driver = webdriver.Chrome()

driver.get('https://www.daraz.com.bd/products/-i466892596-s2246732080.html')

driver.refresh()
driver.maximize_window()

height = driver.execute_script('return document.body.scrollHeight')
print(height) # 1644

for i in range(0, height+2200, 100):
    driver.execute_script(f'window.scrollTo(0, {i});')
    time.sleep(0.5)

# locator same

comment = driver.find_elements(By.CLASS_NAME, 'content')

for i in comment:
    print(i.text)



time.sleep(20)
driver.quit()

