from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.get('https://www.amazon.in')
driver.find_element_by_link_text('Best Sellers').click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.back()