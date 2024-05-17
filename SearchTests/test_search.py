from selenium.webdriver.common.by import By
import unittest
import time
from dotenv import load_dotenv
import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

load_dotenv() 
sys.path.insert(1, os.getenv("CONFIGPATH"))

from DriverConfig import WebDriver
sys.path.insert(1, os.getenv("CONFIGBOOK"))
from page import Page

class UnitTestsSearch(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver=WebDriver()
        cls.driver.initializeDriver()

    def test_search(self):
        self.driver.driver.get(self.driver.url)
        search=Page()
        
        search_box = search.giveInput(self.driver)
        search_box.clear()
        search_box.send_keys("Slayer")
        time.sleep(2)
        
        search_box.send_keys(Keys.DOWN)
        search_box.send_keys(Keys.ENTER)
      

        time.sleep(5)

        search.clickBook(self.driver)

        time.sleep(2)  

        book_details_element =search.getBookName(self.driver)
        self.assertEqual(book_details_element.text, "Slayer")

        self.driver.closeDriver()


     
    @classmethod
    def tearDown(cls):
        cls.driver.closeDriver

if __name__ == "__main__":
    unittest.main()
