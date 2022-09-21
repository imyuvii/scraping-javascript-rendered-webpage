from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Defining the chromedriver path
#DRIVER_BIN = "/opt/homebrew/bin/chromedriver" #MacOS
DRIVER_BIN = "/usr/lib/chromium-browser/chromedriver" #Ubuntu

# Setting up chrome option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

#Creating instance and opening the webpage in new session of chromium browser
browser = webdriver.Chrome(executable_path = DRIVER_BIN)
browser.get('https://demo.vuestorefront.io/c/kitchen')

#defining the variables, It will have array of the selected elements
get_product_name = [product_name.text for product_name in WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.products__grid > div > a > span")))]
get_product_price = [product_price.text for product_price in WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.products__grid > div > div.sf-price")))]

#looping through the variables
for name, price in zip(get_product_name, get_product_price):
  print(f"Product Name: {name} | Price: {price}")
browser.quit()
