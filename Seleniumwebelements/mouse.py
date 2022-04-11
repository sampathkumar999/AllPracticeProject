from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service("C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.find_element(By.XPATH, '//*[@id="txtUsername"]').send_keys('Admin')
driver.find_element(By.XPATH, '//*[@id="txtPassword"]').send_keys('admin123')
driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()

admin_element = driver.find_element(By.XPATH, '//*[@id="menu_admin_viewAdminModule"]')
usermgmt_element = driver.find_element(By.XPATH, '//*[@id="menu_admin_UserManagement"]')
user_element = driver.find_element(By.XPATH, '//*[@id="menu_admin_viewSystemUsers"]')
mouse = ActionChains(driver)
mouse.move_to_element(admin_element).move_to_element(usermgmt_element).move_to_element(user_element).click().perform()