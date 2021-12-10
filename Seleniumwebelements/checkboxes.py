from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_name('txtUsername').send_keys('Admin')
driver.find_element_by_name('txtPassword').send_keys('admin123')
driver.find_element_by_name('Submit').click()
driver.find_element_by_id('menu_admin_viewAdminModule').click()

print(driver.find_element_by_id('ohrmList_chkSelectRecord_32').is_selected())
print(driver.find_element_by_id('ohrmList_chkSelectRecord_6').is_selected())
print(driver.find_element_by_id('ohrmList_chkSelectRecord_34').is_selected())


driver.find_element_by_id('ohrmList_chkSelectRecord_32').click()
driver.find_element_by_id('ohrmList_chkSelectRecord_6').click()
driver.find_element_by_id('ohrmList_chkSelectRecord_34').click()



print(driver.find_element_by_id('ohrmList_chkSelectRecord_32').is_selected())
print(driver.find_element_by_id('ohrmList_chkSelectRecord_6').is_selected())
print(driver.find_element_by_id('ohrmList_chkSelectRecord_34').is_selected())