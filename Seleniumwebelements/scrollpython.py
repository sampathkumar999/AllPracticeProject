from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome(executable_path = "C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.worldometers.info/')
driver.execute_script('window.scrollBy(0,1500)','')
target_element = driver.find_element_by_xpath('/html/body/footer/div[1]/div/a/img')
time.sleep(3)
driver.execute_script('arguments[0].scrollIntoView();',target_element)


