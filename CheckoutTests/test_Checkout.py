from selenium.webdriver.common.by import By
import unittest
import time
from dotenv import load_dotenv
import sys
import os

load_dotenv() 
sys.path.insert(1, os.getenv("CONFIGPATH"))

from DriverConfig import WebDriver

class UnitTestsCheckout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=WebDriver()

        cls.driver.initializeDriver()

    def test_checkout(self):
        self.driver.driver.get(self.driver.url)
        username="hello"
        password="hello123" 
        name = "Maarij"
        address1 = "1234"
        address2 = "1234" 
        pincode = 123456
        state = "Sindh"
        
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "[mattooltip='Login']").click()
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username)
        self.driver.driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Password']")[0].send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()
        time.sleep(2)
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()
        
        time.sleep(2)
        
        
    
        self.driver.driver.find_elements(By.CSS_SELECTOR,"button[tabindex='0']")[2].click()
        time.sleep(2)
        self.driver.driver.find_elements(By.CSS_SELECTOR,"button[tabindex='0']")[3].click()
        time.sleep(2)
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Name']").send_keys(name)
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Address Line 1']").send_keys(address1)
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Address Line 2']").send_keys(address2)
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Pincode']").send_keys(pincode)
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='State']").send_keys(state)
        initial = self.driver.driver.find_elements(By.CSS_SELECTOR, "span#mat-badge-content-0.mat-badge-content.mat-badge-active")[0].text
        time.sleep(2)
        self.driver.driver.find_elements(By.CSS_SELECTOR,"button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base")[0].click()
        time.sleep(7)
        final = self.driver.driver.find_elements(By.CSS_SELECTOR, "span#mat-badge-content-0.mat-badge-content.mat-badge-active")[0].text
        time.sleep(2)
        self.assertEqual(int(initial) - 1,int(final))
     
    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver

if __name__ == "__main__":
    unittest.main()
        