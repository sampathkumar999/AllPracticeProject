from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.get('https://www.reddit.com')
print(driver.get_cookies())
#for cookie in cookies:
 #   print(cookie)
driver.add_cookie({'name':'sampath','domain':'reddit.com','value':'sadhguru'})
print(driver.get_cookies())