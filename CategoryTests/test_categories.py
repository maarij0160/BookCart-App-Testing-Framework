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

class UnitTestsCategories(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=WebDriver()
        cls.driver.initializeDriver()

    def test_click_category_biography(self):
        self.driver.driver.get(self.driver.url)
        
        # Use XPath to locate the element
        category_element = WebDriverWait(self.driver.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-home/div/div[1]/div/app-book-filter/mat-nav-list/mat-list-item[2]"))
        )
        
        # Click on the category element
        category_element.click()

        time.sleep(2)  # Adding a brief pause to allow the page to load
        
        # Click on the specified element
        book_element = self.driver.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div/div[2]/div/div[1]/app-book-card/mat-card/a")
        book_element.click()

        time.sleep(2)  # Adding a brief pause to allow the page to load

        # Assert the text of the specified element
        book_details_element = self.driver.driver.find_element(By.XPATH, "/html/body/app-root/div/app-book-details/mat-card/mat-card-content/div[2]/table/tbody/tr[3]/td[2]")
        self.assertEqual(book_details_element.text, "Biography")

        time.sleep(5)

    def test_click_category_fiction(self):
        self.driver.driver.get(self.driver.url)
        
        # Use XPath to locate the element
        category_element = WebDriverWait(self.driver.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-home/div/div[1]/div/app-book-filter/mat-nav-list/mat-list-item[3]"))
        )
        
        # Click on the category element
        category_element.click()

        time.sleep(2)  # Adding a brief pause to allow the page to load
        
        # Click on the specified element
        book_element = self.driver.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div/div[2]/div/div[1]/app-book-card/mat-card/a")
        book_element.click()

        time.sleep(2)  # Adding a brief pause to allow the page to load

        # Assert the text of the specified element
        book_details_element = self.driver.driver.find_element(By.XPATH, "/html/body/app-root/div/app-book-details/mat-card/mat-card-content/div[2]/table/tbody/tr[3]/td[2]")
        self.assertEqual(book_details_element.text, "Fiction")

        time.sleep(5)


    def test_click_category_mystery(self):
        self.driver.driver.get(self.driver.url)
        
        # Use XPath to locate the element
        category_element = WebDriverWait(self.driver.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-home/div/div[1]/div/app-book-filter/mat-nav-list/mat-list-item[4]"))
        )
        
        # Click on the category element
        category_element.click()

        time.sleep(2)  # Adding a brief pause to allow the page to load
        
        # Click on the specified element
        book_element = self.driver.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div/div[2]/div/div[1]/app-book-card/mat-card/a")
        book_element.click()

        time.sleep(2)  # Adding a brief pause to allow the page to load

        # Assert the text of the specified element
        book_details_element = self.driver.driver.find_element(By.XPATH, "/html/body/app-root/div/app-book-details/mat-card/mat-card-content/div[2]/table/tbody/tr[3]/td[2]")
        self.assertEqual(book_details_element.text, "Mystery")

        time.sleep(5)    

    def test_click_category_fantasy(self):
        self.driver.driver.get(self.driver.url)
        
        # Use XPath to locate the element
        category_element = WebDriverWait(self.driver.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-home/div/div[1]/div/app-book-filter/mat-nav-list/mat-list-item[5]"))
        )
        
        # Click on the category element
        category_element.click()

        time.sleep(2)  # Adding a brief pause to allow the page to load
        
        # Click on the specified element
        book_element = self.driver.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div/div[2]/div/div[1]/app-book-card/mat-card/a")
        book_element.click()

        time.sleep(2)  # Adding a brief pause to allow the page to load

        # Assert the text of the specified element
        book_details_element = self.driver.driver.find_element(By.XPATH, "/html/body/app-root/div/app-book-details/mat-card/mat-card-content/div[2]/table/tbody/tr[3]/td[2]")
        self.assertEqual(book_details_element.text, "Fantasy")

        time.sleep(5)
    

    def test_click_category_romance(self):
        self.driver.driver.get(self.driver.url)
        
        # Use XPath to locate the element
        category_element = WebDriverWait(self.driver.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-home/div/div[1]/div/app-book-filter/mat-nav-list/mat-list-item[6]"))
        )
        
        # Click on the category element
        category_element.click()

        time.sleep(2)  # Adding a brief pause to allow the page to load
        
        # Click on the specified element
        book_element = self.driver.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div/div[2]/div/div[1]/app-book-card/mat-card/a")
        book_element.click()

        time.sleep(2)  # Adding a brief pause to allow the page to load

        # Assert the text of the specified element
        book_details_element = self.driver.driver.find_element(By.XPATH, "/html/body/app-root/div/app-book-details/mat-card/mat-card-content/div[2]/table/tbody/tr[3]/td[2]")
        self.assertEqual(book_details_element.text, "Romance")

        time.sleep(5)

     
    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver

if __name__ == "__main__":
    unittest.main()
