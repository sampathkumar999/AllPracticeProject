from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome(executable_path = "C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
browser.get('https://www.yatra.com/')
browser.maximize_window()
wait = WebDriverWait(browser, 10)
wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']"))).click()
wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']"))).send_keys('Mumbai')

wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']"))).send_keys('New york')
