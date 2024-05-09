import sys
import os
from dotenv import load_dotenv

load_dotenv() 
sys.path.insert(1, os.getenv("CONFIGPATH"))

from DriverConfig import WebDriver
from selenium.webdriver.common.by import By
import unittest
import time

class UnitTestsRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=WebDriver()

        cls.driver.initializeDriver()


    def test_InvalidRegister(self):
        
        self.driver.driver.get(self.driver.url)
        firstName="Muhammad"
        lastName="Faheem"
        username="Maarij69"
        password="Temp1234"
        
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "[mattooltip='Login']").click()
        self.driver.driver.find_elements(By.CSS_SELECTOR,"button[tabindex='0']")[3].click()
    
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='First name']").send_keys(firstName)
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']").send_keys(lastName)
        
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='User name']").send_keys(username)
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Confirm Password']").send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "mat-radio-button[value='Male']").click()
        time.sleep(5)
        
        try:
            reg_button = self.driver.find_element(By.CLASS_NAME, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base")[0]
            if reg_button.is_enabled():
                reg_button.click()
        except:
            pass
        
    def test_validRegister(self):
        self.driver.driver.get(self.driver.url)
        firstName="Muhammad"
        lastName="Faheem"
        username="Maarij69"
        password="Temp1234"
        
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "[mattooltip='Login']").click()
        self.driver.driver.find_elements(By.CSS_SELECTOR,"button[tabindex='0']")[3].click()
    
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='First name']").send_keys(firstName)
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']").send_keys(lastName)
        
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='User name']").send_keys(username)
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Confirm Password']").send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "mat-radio-button[value='Male']").click()
        
        time.sleep(5)
        self.driver.driver.find_elements(By.CSS_SELECTOR,"button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base")[0].click()
        
        time.sleep(5)
        header = self.driver.driver.find_element(By.CSS_SELECTOR,"mat-card-title.mat-mdc-card-title.mat-h1").text
        self.assertEqual(header,'Login')
        
    
        
    
       
    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver()

if __name__ == "__main__":
    unittest.main()
    
        