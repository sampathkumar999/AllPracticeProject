import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.get('http://demo.guru99.com/test/newtours/')
driver.maximize_window()
path = 'C://Users/sadguru/PycharmProjects/AllPracticeProject/excelpractice/book2.xlsx'
rows = XLUtils.getRowCount(path, 'Sheet1')
count = rows + 1
for r in range(2, count):
    username = XLUtils.readData(path, 'Sheet1', r, 1)
    password = XLUtils.readData(path, 'Sheet1', r, 2)

    driver.find_element(By.NAME, 'userName').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)

    driver.find_element(By.NAME, 'submit').click()
    if driver.title == 'Login: Mercury Tours':
        print('test is passed')
        XLUtils.writeData(path, 'Sheet1', r, 3, 'passed')
    else:
        print('test is failed')
        XLUtils.writeData(path, 'Sheet1', r, 3, 'failed')
    driver.find_element(By.XPATH, "//a[normalize-space()='Home']").click()














