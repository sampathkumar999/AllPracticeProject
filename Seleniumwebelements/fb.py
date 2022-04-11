from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path = "C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.get("https://www.geeksforgeeks.org/")

# create action chain object
action = ActionChains(driver)

# perform the operation
action.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()