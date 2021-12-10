from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome(executable_path = "C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-tree.html")
driver.switch_to.frame('packageListFrame')
Element1 = driver.find_element_by_xpath('/html/body/main/ul/li[1]/a')
Element1.click()
driver.switch_to.default_content()
driver.switch_to.frame('packageFrame')
Element2 = driver.find_element_by_xpath('/html/body/main/div/section[1]/ul/li[14]/a')
Element2.click()
driver.switch_to.default_content()
driver.switch_to.frame('classFrame')
print(driver.title)
Element3 = driver.find_element_by_xpath('/html/body/header/nav/div[1]/div[1]/ul/li[6]/a')
Element3.click()



