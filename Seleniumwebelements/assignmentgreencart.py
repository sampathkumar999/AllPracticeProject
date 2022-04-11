from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element(By.CLASS_NAME, 'search-keyword').send_keys('ber')
time.sleep(3)
mylist = []
names = driver.find_elements(By.XPATH,'//h4[@class="product-name"]')

assert len(names) == 3
for name in names:
    mylist.append(name.text)

print(mylist)