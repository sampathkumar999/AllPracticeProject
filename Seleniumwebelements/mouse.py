from selenium import webdriver
from selenium.webdriver import ActionChains

import time
driver = webdriver.Chrome(executable_path = "C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.find_element_by_xpath('//*[@id="txtUsername"]').send_keys('Admin')
driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys('admin123')
driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

admin_element = driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]')
usermgmt_element = driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
user_element = driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')
mouse=ActionChains(driver)
mouse.move_to_element(admin_element).move_to_element(usermgmt_element).move_to_element(user_element).click().perform()