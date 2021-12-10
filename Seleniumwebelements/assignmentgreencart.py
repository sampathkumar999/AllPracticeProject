from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element_by_class_name('search-keyword').send_keys('ber')
time.sleep(3)
mylist = []
names = driver.find_elements_by_xpath('//h4[@class="product-name"]')

assert len(names) == 3
#for name in names:
 #   mylist.append(name.text)
#print(mylist)