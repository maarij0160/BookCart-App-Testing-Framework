from selenium.webdriver.common.by import By
import unittest
import time
from dotenv import load_dotenv
import sys
import os


load_dotenv() 
sys.path.insert(1, os.getenv("CONFIGPATH"))

from DriverConfig import WebDriver

class UnitTestsLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=WebDriver()

        cls.driver.initializeDriver()

   
    def test_validLogin(self):
        self.driver.driver.get(self.driver.url)
        username="hello"
        password="hello123" 
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "[mattooltip='Login']").click()
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username)
        self.driver.driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Password']")[0].send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()
        time.sleep(2)
        header = self.driver.driver.find_element(By.CSS_SELECTOR,"a.mat-mdc-menu-trigger.mdc-button.mdc-button--unelevated.mat-mdc-unelevated-button.mat-primary.mat-mdc-button-base.ng-star-inserted").text
        
        header = header.split("\n")[-1]
        self.assertEqual(header,username)
        
    def test_InvalidLogin(self):
        
        self.driver.driver.get(self.driver.url)
        username="hello"
        password="hello" 
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "[mattooltip='Login']").click()
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username)
        self.driver.driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Password']")[0].send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()
        time.sleep(2)
        text = self.driver.driver.find_element(By.CSS_SELECTOR,"mat-error#mat-mdc-error-0.mat-mdc-form-field-error.mat-mdc-form-field-bottom-align").text
        
        
        self.assertEqual(text,"Username or Password is incorrect.")
        
    
     
    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver

if __name__ == "__main__":
    unittest.main()
      