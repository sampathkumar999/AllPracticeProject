from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\Users\\sadguru\\Downloads\\chromedriver.exe")

def login():

    driver.get("https://www.instagram.com/")
    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')

    username.send_keys('7013651220')
    password.send_keys('samp666ath')

    button = driver.find_element_by_xpath('//div[@class="                     Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                              "]')
    button.click()


login()