from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_name('txtUsername').send_keys('Admin')
driver.find_element_by_name('txtPassword').send_keys('admin123')
driver.find_element_by_name('Submit').click()
driver.find_element_by_id('menu_admin_viewAdminModule').click()
text = driver.find_element_by_xpath("//tr[2]").text
print(text)