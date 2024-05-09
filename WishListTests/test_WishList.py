from selenium.webdriver.common.by import By
import unittest
import time
from dotenv import load_dotenv, dotenv_values 
import sys
import os

load_dotenv() 
sys.path.insert(1, os.getenv("CONFIGPATH"))

from DriverConfig import WebDriver

class UnitTestsWishList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=WebDriver()

        cls.driver.initializeDriver()

    def test_addtoList(self):
        
        self.driver.driver.get(self.driver.url)
        username="hello"
        password="hello123" 
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "[mattooltip='Login']").click()
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username)
        self.driver.driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Password']")[0].send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()
        time.sleep(2)
        initial = self.driver.driver.find_element(By.CSS_SELECTOR,"body > app-root > app-nav-bar > mat-toolbar > mat-toolbar-row > div.d-flex.align-items-center > button.mdc-icon-button.mat-mdc-icon-button.mat-unthemed.mat-mdc-button-base.ng-star-inserted").text
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "body > app-root > div > app-home > div > div.col.mb-3 > div > div:nth-child(1) > app-book-card > mat-card > mat-card-content > div.favourite.mat-elevation-z8.ng-star-inserted > app-addtowishlist > span").click()
        
        time.sleep(2)
        final = self.driver.driver.find_element(By.CSS_SELECTOR, "body > app-root > app-nav-bar > mat-toolbar > mat-toolbar-row > div.d-flex.align-items-center > button.mdc-icon-button.mat-mdc-icon-button.mat-unthemed.mat-mdc-button-base.ng-star-inserted").text
        
        initial = initial.split("\n")[-1]
        final = final.split("\n")[-1]
        self.assertEqual(int(initial) + 1,int(final))
        
    def test_removefromList(self):
        
        self.driver.driver.get(self.driver.url)
        username="hello"
        password="hello123" 
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "[mattooltip='Login']").click()
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username)
        self.driver.driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Password']")[0].send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()
        time.sleep(2)
        initial = self.driver.driver.find_element(By.CSS_SELECTOR,"body > app-root > app-nav-bar > mat-toolbar > mat-toolbar-row > div.d-flex.align-items-center > button.mdc-icon-button.mat-mdc-icon-button.mat-unthemed.mat-mdc-button-base.ng-star-inserted").text
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "body > app-root > div > app-home > div > div.col.mb-3 > div > div:nth-child(1) > app-book-card > mat-card > mat-card-content > div.favourite.mat-elevation-z8.ng-star-inserted > app-addtowishlist > span").click()
        
        time.sleep(2)
        final = self.driver.driver.find_element(By.CSS_SELECTOR, "body > app-root > app-nav-bar > mat-toolbar > mat-toolbar-row > div.d-flex.align-items-center > button.mdc-icon-button.mat-mdc-icon-button.mat-unthemed.mat-mdc-button-base.ng-star-inserted").text
        
        initial = initial.split("\n")[-1]
        final = final.split("\n")[-1]
        self.assertEqual(int(initial) - 1,int(final))
        
        
    def test_clearList(self):
        
        self.driver.driver.get(self.driver.url)
        username="hello"
        password="hello123" 
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "[mattooltip='Login']").click()
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username)
        self.driver.driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Password']")[0].send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()
        time.sleep(2)
        
        self.driver.driver.find_elements(By.CSS_SELECTOR,"button[tabindex='0']")[1].click()
        
        time.sleep(2)
        self.driver.driver.find_element(By.CSS_SELECTOR,"button.mat-elevation-z4.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-unthemed.mat-mdc-button-base").click()
        time.sleep(2)
        final = self.driver.driver.find_element(By.CSS_SELECTOR, "body > app-root > app-nav-bar > mat-toolbar > mat-toolbar-row > div.d-flex.align-items-center > button.mdc-icon-button.mat-mdc-icon-button.mat-unthemed.mat-mdc-button-base.ng-star-inserted").text
        final = final.split("\n")[-1]
        self.assertEqual(int(final),0)
        
     
    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver

if __name__ == "__main__":
    unittest.main()
        