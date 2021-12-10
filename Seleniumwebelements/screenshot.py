from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path = "C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.get('https://www.google.com')
#driver.save_screenshot('E:\copy of python\screenshots\google2.jpg')
driver.get_screenshot_as_file('E:\copy of python\screenshots\googlee.png')
