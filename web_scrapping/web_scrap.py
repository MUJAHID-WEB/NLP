from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()
driver.get('https://innovativeskillsbd.com/?t=1742027478937')

driver.maximize_window()

# text = driver.find_element(By.XPATH, '/html/body/section[4]/div/div/ul/li[2]/div/div[2]/a').text

# link = driver.find_element(By.XPATH, '/html/body/section[4]/div/div/ul/li[2]/div/div[2]/a').get_attribute('href')

# image = driver.find_element(By.XPATH, '/html/body/section[4]/div/div/ul/li[2]/div/div[1]/img').get_attribute('src')

text_list = []
link_list = []
image_list = []
for i in range(1,4):
    j = str(i)
    text2 = driver.find_element(By.XPATH, '/html/body/section[4]/div/div/ul/li['+j+']/div/div[2]/a').text
    link2 = driver.find_element(By.XPATH, '/html/body/section[4]/div/div/ul/li['+j+']/div/div[2]/a').get_attribute('href')
    image2 = driver.find_element(By.XPATH, '/html/body/section[4]/div/div/ul/li['+j+']/div/div[1]/img').get_attribute('src')
    
    text_list.append(text2)
    link_list.append(link2)
    image_list.append(image2)
    
print(text_list)
print(link_list)
print(image_list)

# print(text)
# print(link)
# print(image)


time.sleep(20)
driver.quit()


