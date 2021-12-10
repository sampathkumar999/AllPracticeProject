import XLUtils
from selenium import webdriver
driver = webdriver.Chrome(executable_path = "C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.get('http://demo.guru99.com/test/newtours/')
driver.maximize_window()
path = 'C://excel sheets/book2.xlsx'
rows = XLUtils.getRowCount(path,'book2')
count = rows + 1
for r in  range(2, count):
    username = XLUtils.readData(path,'book2',r,1)
    password = XLUtils.readData(path,'book2',r,2)

    driver.find_elements_by_name('userName').send_keys(username)
    driver.find_elements_by_name('password').send_keys(password)

    driver.find_element_by_name('submit').click()
    if driver.title=='Login: Mercury Tours':
        print('test is passed')
        XLUtils.writeData(path,'book2',r,3,'passed')
    else:
        print('test is failed')
        XLUtils.writeData(path,'book2',r,3,'failed')


    driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr/td[1]'
                                 '/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/font/a').click()











