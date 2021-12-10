from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
print(driver.current_url)
print(driver.title)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/nav/div/div/ul/li[1]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/nav/div/div/ul/li[1]/ul/li[2]/a").click()
driver.close()
