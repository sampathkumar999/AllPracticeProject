from selenium import webdriver
from selenium.webdriver.support.ui import select

driver = webdriver.Chrome(executable_path = "C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.expedia.co.in/")
driver.find_element_by_xpath("//*[@id='uitk-tabs-button-container']/li[2]/a/span").click()
element = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[4]/div/div[1]/div/div/div/div/div/"
                             "div[2]/div/form/div[2]/div/div[1]/div[1]/div/div[2]/div/a/svg")
drop = select(element)
drop.select_visible_text("First class")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[4]/div/div[1]/div/div/div/div/div/"
                             "div[2]/div/form/div[2]/div/div[1]/div[1]/div/div[2]/div/div/div/a[4]/span")
driver.find_element_by_xpath("").send_keys("BOM")
driver.find_element_by_xpath("//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[1]/div/div[2]/div/div/div/button").send_keys("NYC")
driver.find_element_by_xpath("//*[@id='d1-btn']").send_keys("25 jun")
driver.find_element_by_xpath("//*[@id='d2-btn']").send_keys("30 jun")
driver.find_element_by_xpath("//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button").click()



