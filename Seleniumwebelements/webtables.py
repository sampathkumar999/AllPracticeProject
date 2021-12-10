from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\\Users\\sadguru\\Downloads\\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")
driver.maximize_window()


rows = driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr")
RowCount = len(rows)
print(RowCount)
Columns = driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr/th")
ColumnCount = len(Columns)
print(ColumnCount)

for row in range(2, RowCount+1):

    for col in range(1, ColumnCount+1):

        Text = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr[" + str(row) + "]/td[" + str(col) + "]").text

        print(Text, end='   ')

    print()
