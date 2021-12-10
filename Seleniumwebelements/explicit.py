from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome(executable_path= "c:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.get('https://app.hubspot.com/login')

wait = WebDriverWait(driver, 10)
email_id = wait.until(ec.presence_of_element_located((By.ID,'username')))
email_id.send_keys('naveen@gmail.com')
driver.find_element_by_id('password').send_keys('test@123')
wait = WebDriverWait(driver, 10)
login = wait.until(ec.element_to_be_clickable((By.ID,'password-login-button')))
login.click()


#driver.find_element_by_name('').click()