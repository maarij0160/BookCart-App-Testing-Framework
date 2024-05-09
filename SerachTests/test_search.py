from selenium.webdriver.common.by import By
import unittest
import time
from dotenv import load_dotenv, dotenv_values 
import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

load_dotenv() 
sys.path.insert(1, os.getenv("CONFIGPATH"))

from DriverConfig import WebDriver

class UnitTestsSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=WebDriver()
        cls.driver.initializeDriver()

    def test_click_category_biography(self):
        self.driver.driver.get(self.driver.url)
        
        # Use XPath to locate the element
        search_box = WebDriverWait(self.driver.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-nav-bar/mat-toolbar/mat-toolbar-row/div[2]/app-search/form/input"))
        )
        
        # Clear any existing text in the search box
        search_box.clear()
        
        # Enter "slayer" into the search box
        search_box.send_keys("Slayer")
        time.sleep(2)
        search_box.send_keys(Keys.DOWN)
        
        # Press Enter to submit the search
        search_box.send_keys(Keys.ENTER)
      

        time.sleep(5)

       
        
        # Click on the specified element
        book_element = self.driver.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div/div[2]/div/div[1]/app-book-card/mat-card/a")
        book_element.click()

        time.sleep(2)  # Adding a brief pause to allow the page to load

        # Assert the text of the specified element
        book_details_element = self.driver.driver.find_element(By.XPATH, "/html/body/app-root/div/app-book-details/mat-card/mat-card-content/div[2]/table/tbody/tr[1]/td[2]")
        self.assertEqual(book_details_element.text, "Slayer")

        time.sleep(5)


     
    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver

if __name__ == "__main__":
    unittest.main()
