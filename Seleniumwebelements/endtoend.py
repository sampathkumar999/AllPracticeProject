from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.implicitly_wait(7)
driver.get('https://rahulshettyacademy.com/angularpractice/#/')
driver.maximize_window()
driver.find_element_by_xpath('//a[@class="nav-link" and text()="Shop"]').click()
mobiles = driver.find_elements_by_xpath('//app-card//div//div//h4//a')
for mobile in mobiles:
    if mobile.text == 'iphone X':
        driver.find_element_by_xpath('//app-card[1]//div//div[2]//button[@class="btn btn-info"]').click()
        break

driver.find_element_by_xpath('//a[@class="nav-link btn btn-primary"]').click()
name = driver.find_element_by_xpath('//tr//td[1]//div//div//h4//a').text
assert name == 'iphone X'

driver.find_element_by_xpath('/html/body/app-root/app-shop/div/div/div/table/tbody/tr[3]/td[5]/button').click()
driver.find_element_by_id('country').send_keys('India')
driver.find_element_by_xpath('/html/body/app-root/app-shop/div/app-checkout/div/div[2]/ul[1]/li/a').click()
#driver.find_element_by_xpath('//input[@id="checkbox2"]').click()
driver.find_element_by_xpath('//input[@type="submit"]').click()
confirm = driver.find_element_by_xpath('/html/body/app-root/app-shop/div/app-checkout/div[2]/div').text
assert 'Success! Thank you!' in confirm



