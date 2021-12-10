from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.find_element_by_name('proceed').click()
alertt = driver.switch_to.alert
print(alertt.text)
alertt.accept()