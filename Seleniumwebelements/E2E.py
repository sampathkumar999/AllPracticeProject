from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(executable_path='C:\\Users\\sadguru\\Downloads\\chromedriver.exe')
browser.get('http://automationpractice.com/index.php')
browser.maximize_window()
