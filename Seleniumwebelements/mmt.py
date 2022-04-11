from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(executable_path='C:\\Users\\sadguru\\Downloads\\chromedriver.exe')
browser.get('https://www.makemytrip.com/')
browser.maximize_window()
time.sleep(2)
browser.find_element(By.XPATH, "//input[@placeholder='From']").click()
browser.find_element(By.XPATH, "//input[@placeholder='From']").send_keys('new')
options = browser.find_elements(By.XPATH,'//ul[@role="listbox"]/li')
for place in options:
    if place.text == 'New Stuyahok, United States':
        place.click()
        break

