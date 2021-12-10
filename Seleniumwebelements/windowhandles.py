from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.get('https://www.apty.io/')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="hs_menu_wrapper_module_155997681726813_"]/ul/li[5]').click()
driver.find_element_by_xpath('//*[@id="hs_cos_wrapper_module_1590015026590577"]/div/a').click()
print(driver.current_window_handle)
handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

