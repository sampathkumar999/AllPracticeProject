import unittest
from selenium import webdriver

class searchenginetest(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(executable_path= "c:\\Users\\sadguru\\Downloads\\chromedriver.exe")
        self.driver.get('https://www.google.com')
        print('The title of the page is:',self.driver.title)
        self.driver.close()


    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path= "c:\\Users\\sadguru\\Downloads\\chromedriver.exe")
        self.driver.get('https://bing.com')
        print('The title of the page is:', self.driver.title)
        self.driver.close()


if __name__ =="__main__":
    unittest.main()
