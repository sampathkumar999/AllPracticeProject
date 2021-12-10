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
driver.find_element_by_id('menu_leave_viewLeaveModule').click()
driver.find_element_by_id('menu_leave_viewMyLeaveList').click()
driver.find_element_by_id('calFromDate').clear()
driver.find_element_by_id('calFromDate').send_keys('2021-06-01')
driver.find_element_by_id('calToDate').clear()
driver.find_element_by_id('calToDate').send_keys('2021-12-31')
driver.find_element_by_id('leaveList_chkSearchFilter_checkboxgroup_allcheck').click()
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
for box in checkboxes:
    box.click()

driver.find_element_by_name('btnSearch').click()