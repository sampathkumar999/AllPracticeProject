from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path = "C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_name('txtUsername').send_keys('Admin')
driver.find_element_by_name('txtPassword').send_keys('admin123')
driver.find_element_by_name('Submit').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="menu_recruitment_viewRecruitmentModule"]/b').click()
driver.find_element_by_xpath('//*[@id="menu_recruitment_viewJobVacancy"]').click()
columns = len(driver.find_elements_by_xpath('//*[@id="resultTable"]/thead/tr/th'))
rows = len(driver.find_elements_by_xpath('//*[@id="resultTable"]/tbody/tr'))
print(rows)
print(columns)
for r in range(1,rows+1):
        print(driver.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr['+str(r)+']').text)



