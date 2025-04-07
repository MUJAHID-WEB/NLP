from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

driver = webdriver.Chrome()

driver.get('https://www.rokomari.com/book/category/372/prophets-messengers-sahaba-tabei-oli-awliya?sort=DISCOUNT_DESC&ratings=&page=')

driver.maximize_window()

total_product_text = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/section[2]/div[1]/div/div/p').text

print(total_product_text)  # (Showing 1 to 60 of 1939 items)

# pattern = r'of (\d+) items'
# match = re.search(pattern, total_product_text)

# if match:
#     total_product = match.group(1)
#     print(total_product)


pattern = total_product_text.split()

print(pattern) # ['(Showing', '1', 'to', '60', 'of', '1939', 'items)']

total_product = 0
total_product = pattern[5]
total_pages = round(int(total_product)/60)

print(total_product)  # 1939
print(total_pages)  #32.316666 = 32 pages


text_list = []
link_list = []
image_list = []

for page in range(1, total_pages+1):
    p = str(page)
    driver.get(f'https://www.rokomari.com/book/category/372/prophets-messengers-sahaba-tabei-oli-awliya?sort=DISCOUNT_DESC&ratings=&page={p}')  # pagination wise parent url

    driver.maximize_window()

    products = driver.find_elements(By.XPATH, '/html/body/div[7]/div/div/div/section[2]/div[2]/div/div')  # all products in a page

    for i in range(len(products)):
        j = i + 1
        text2 = driver.find_element(By.XPATH, f'/html/body/div[7]/div/div/div/section[2]/div[2]/div/div[{j}]/div/a/div[2]/h4').text

        link2 = driver.find_element(By.XPATH, f'/html/body/div[7]/div/div/div/section[2]/div[2]/div/div[{j}]/div/a').get_attribute('href')

        image2 = driver.find_element(By.XPATH, f'/html/body/div[7]/div/div/div/section[2]/div[2]/div/div[{j}]/div/a/div[1]/img').get_attribute('src')
        
        text_list.append(text2)
        link_list.append(link2)
        image_list.append(image2)
        
    print(text_list)
    print(link_list)
    print(image_list)




time.sleep(20)
driver.quit()


