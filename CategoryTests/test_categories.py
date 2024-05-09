from selenium.webdriver.common.by import By
import unittest
import time
from dotenv import load_dotenv
import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv() 
sys.path.insert(1, os.getenv("CONFIGPATH"))

from DriverConfig import WebDriver
sys.path.insert(1, os.getenv("CONFIGBOOK"))
from page import Page


class UnitTestsCategories(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=WebDriver()
        cls.driver.initializeDriver()

    def test_click_category_biography(self):
        self.driver.driver.get(self.driver.url)
        
        category=Page()
        category_element = category.clickBiography(self.driver) 
        category_element.click()

        time.sleep(2) 
        
    
        category.clickBook(self.driver)

        time.sleep(2) 

        book_details_element = category.getBookCategory(self.driver)
        self.assertEqual(book_details_element.text, "Biography")

        time.sleep(5)

    def test_click_category_fiction(self):
        self.driver.driver.get(self.driver.url)
        
        category=Page()
        category_element = category.clickFiction(self.driver) 
        category_element.click()

        time.sleep(2)
        
        category.clickBook(self.driver)

        time.sleep(2) 
        book_details_element = category.getBookCategory(self.driver)
        self.assertEqual(book_details_element.text, "Fiction")

        time.sleep(5)



    def test_click_category_mystery(self):
        self.driver.driver.get(self.driver.url)
        
        category=Page()
        category_element = category.clickMystery(self.driver) 
        category_element.click()

        time.sleep(2)  
        
        category.clickBook(self.driver)

        time.sleep(2)  

        
        book_details_element = category.getBookCategory(self.driver)
        self.assertEqual(book_details_element.text, "Mystery")

        time.sleep(5)

    def test_click_category_fantasy(self):
        self.driver.driver.get(self.driver.url)
        
        category=Page()
        category_element = category.clickFantasy(self.driver) 
        category_element.click()

        time.sleep(2)  
        
        category.clickBook(self.driver)
        
        time.sleep(2)  

        
        book_details_element = category.getBookCategory(self.driver)
        self.assertEqual(book_details_element.text, "Fantasy")

        time.sleep(5)

    def test_click_category_romance(self):
        self.driver.driver.get(self.driver.url)
        
        category=Page()
        category_element = category.clickRomance(self.driver) 
        category_element.click()

        time.sleep(2)  
        
        category.clickBook(self.driver)
        
        time.sleep(2)  

        
        book_details_element = category.getBookCategory(self.driver)
        self.assertEqual(book_details_element.text, "Romance")

        time.sleep(5)

     
    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver

if __name__ == "__main__":
    unittest.main()
