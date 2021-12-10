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
driver.find_element_by_id('menu_recruitment_viewRecruitmentModule').click()
#vacancy = driver.find_element_by_name('candidateSearch[jobVacancy]')
#dropdown = Select(vacancy)
#dropdown.select_by_value('5')
#jobtitle = driver.find_element_by_name('candidateSearch[jobTitle]')
#dropdown = Select(jobtitle)
#dropdown.select_by_visible_text('Software Engineer')


#counting all options

#print(len(dropdown.options))

#printing all options

#all_options = dropdown.options
#for option in all_options:
    #print(option.text)

table = driver.find_elements_by_xpath("//tr[@class='even']")
for item in table:
    print(item.text)
    item.click()



