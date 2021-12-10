from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element_by_class_name('search-keyword').send_keys('ber')
time.sleep(3)
mylist = []
names = driver.find_elements_by_xpath('//h4[@class="product-name"]')
for name in names:
    mylist.append(name.text)
print(mylist)
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()

driver.find_element_by_xpath('//*[@id="root"]/div/header/div/div[3]/a[4]/img').click()
driver.find_element_by_xpath('//button[text()="PROCEED TO CHECKOUT"]').click()
driver.find_element_by_class_name('promoCode').send_keys('rahulshettyacademy')
driver.find_element_by_class_name('promoBtn').click()
mylist2 = []
cartnames = driver.find_elements_by_xpath('//p[@class="product-name"]')
for item in cartnames:
    mylist2.append(item.text)
print(mylist2)
assert mylist == mylist2


