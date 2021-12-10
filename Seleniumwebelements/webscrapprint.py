from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.amazon.in')
driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']").send_keys('samsung phones')
driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]').click()
phone_names = driver.find_elements_by_xpath("//span[contains(@class,'a-color-base a-text-normal')]")
phone_prices = driver.find_elements_by_xpath("//span[contains(@class,'price-whole')]")

for phone in phone_names:
    print(phone.text)

print('*'*50)

for price in phone_prices:
    print(price.text)





