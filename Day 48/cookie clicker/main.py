import threading
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_file_path = r'YOUR WEDRIVER FILE PATH'

service = Service(chrome_file_path)
driver = webdriver.Chrome(service=service)

driver.get('https://orteil.dashnet.org/cookieclicker/')

lan = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="langSelect-EN"]'))
)
lan.click()


def able():
    try:
    
        pro = driver.find_elements(By.CLASS_NAME, 'product unlocked enable')

        if len(pro) > 0:
      
            pro[-1].click()
        else:
            print("No products to click.")

        threading.Timer(10, able).start()
    except StaleElementReferenceException:
        print("Element is stale, retrying...")



able()

while True:
    try:
   
        cookie = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="bigCookie"]'))
        )
        cookie.click()  
    except StaleElementReferenceException:
        print("Cookie element is stale, retrying...")

driver.quit()
