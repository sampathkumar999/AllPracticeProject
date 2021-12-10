from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path = "C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()

driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/"
                             "table/tbody/tr[2]/td[2]/a").click()
roundtrip_radio_element = driver.find_element_by_css_selector("input[value = roundtrip]")
print('status of roundtrip radio button:',roundtrip_radio_element.is_selected())

oneway_radio_element = driver.find_element_by_css_selector("input[value = oneway]")
print('status of roundtrip radio button:',oneway_radio_element.is_selected())






