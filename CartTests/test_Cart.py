from selenium.webdriver.common.by import By
import unittest
import time
from dotenv import load_dotenv
import sys
import os

load_dotenv() 
sys.path.insert(1, os.getenv("CONFIGPATH"))

from DriverConfig import WebDriver

class UnitTestsCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=WebDriver()

        cls.driver.initializeDriver()

    def test_addtocart(self):
        
        self.driver.driver.get(self.driver.url)
        username="hello"
        password="hello123" 
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "[mattooltip='Login']").click()
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username)
        self.driver.driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Password']")[0].send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()
        time.sleep(2)
        initial = self.driver.driver.find_elements(By.CSS_SELECTOR, "span#mat-badge-content-0.mat-badge-content.mat-badge-active")[0].text
        self.driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()
        
        time.sleep(2)
        final = self.driver.driver.find_elements(By.CSS_SELECTOR, "span#mat-badge-content-0.mat-badge-content.mat-badge-active")[0].text
        
        self.assertEqual(int(initial) + 1,int(final))
        time.sleep(5)
        
    
        
    def test_incQty(self):
        
        self.driver.driver.get(self.driver.url)
        username="hello"
        password="hello123" 
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "[mattooltip='Login']").click()
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username)
        self.driver.driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Password']")[0].send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()
        time.sleep(2)
        self.driver.driver.find_elements(By.CSS_SELECTOR,"button[tabindex='0']")[2].click()
        time.sleep(2)
        initial = self.driver.driver.find_element(By.CSS_SELECTOR, "div.d-flex.align-items-center > div:nth-child(2)").text
        self.driver.driver.find_element(By.CSS_SELECTOR,"td.mat-mdc-cell.mat-column-quantity > div > div:nth-child(3) > button").click()
        time.sleep(2)
        final = self.driver.driver.find_element(By.CSS_SELECTOR, "div.d-flex.align-items-center > div:nth-child(2)").text
        time.sleep(2)
        self.assertEqual(int(initial) + 1,int(final))
        time.sleep(5)
        
    def test_decQty(self):
        
        self.driver.driver.get(self.driver.url)
        username="hello"
        password="hello123" 
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "[mattooltip='Login']").click()
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username)
        self.driver.driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Password']")[0].send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()
        time.sleep(2)
        self.driver.driver.find_elements(By.CSS_SELECTOR,"button[tabindex='0']")[2].click()
        time.sleep(2)
        initial = self.driver.driver.find_element(By.CSS_SELECTOR, "div.d-flex.align-items-center > div:nth-child(2)").text
        self.driver.driver.find_element(By.CSS_SELECTOR,"td.mat-mdc-cell.mat-column-quantity > div > div:nth-child(1) > button").click()
        time.sleep(2)
        final = self.driver.driver.find_element(By.CSS_SELECTOR, "div.d-flex.align-items-center > div:nth-child(2)").text
        time.sleep(2)
        self.assertEqual(int(initial) - 1,int(final))
        time.sleep(5)
        
    def test_deleteItem(self):
        
            
        self.driver.driver.get(self.driver.url)
        username="hello"
        password="hello123" 
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "[mattooltip='Login']").click()
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username)
        self.driver.driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Password']")[0].send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()
        time.sleep(2)
        self.driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()
        time.sleep(2)
        self.driver.driver.find_elements(By.CSS_SELECTOR,"button[tabindex='0']")[2].click()
        time.sleep(2)
        initialcart = self.driver.driver.find_elements(By.CSS_SELECTOR, "span#mat-badge-content-0.mat-badge-content.mat-badge-active")[0].text
        itemcount = self.driver.driver.find_element(By.CSS_SELECTOR, "div.d-flex.align-items-center > div:nth-child(2)").text
        self.driver.driver.find_element(By.CSS_SELECTOR,"body > app-root > div > app-shoppingcart > mat-card > mat-card-content.mat-mdc-card-content.my-3.ng-star-inserted > table > tbody > tr > td.mat-mdc-cell.mdc-data-table__cell.cdk-cell.cdk-column-action.mat-column-action.ng-star-inserted > button").click()
        time.sleep(2)
        
        final = self.driver.driver.find_elements(By.CSS_SELECTOR, "span#mat-badge-content-0.mat-badge-content.mat-badge-active")[0].text
        time.sleep(2)
        self.assertEqual(int(initialcart) - int(itemcount),int(final))
        time.sleep(5)
            
    def test_clearcart(self):
        
        self.driver.driver.get(self.driver.url)
        username="hello"
        password="hello123" 
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "[mattooltip='Login']").click()
        self.driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username)
        self.driver.driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Password']")[0].send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()
        time.sleep(2)
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()
        time.sleep(2)
        
        self.driver.driver.find_elements(By.CSS_SELECTOR,"button[tabindex='0']")[2].click()
        
        time.sleep(2)
        self.driver.driver.find_elements(By.CSS_SELECTOR,"body > app-root > div > app-shoppingcart > mat-card > mat-card-header > div.ng-star-inserted > button")[0].click()
        time.sleep(2)
        final = self.driver.driver.find_elements(By.CSS_SELECTOR, "span#mat-badge-content-0.mat-badge-content.mat-badge-active")[0].text
        self.assertEqual(int(final),0)
      
        time.sleep(5)
        
    
     
    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver

if _name_ == "_main_":
    #unittest.main()
    test_cases = [UnitTestsCart('test_addtocart'), 
                  UnitTestsCart('test_incQty'), 
                  UnitTestsCart('test_decQty'), 
                  UnitTestsCart('test_deleteItem'), 
                  UnitTestsCart('test_clearcart')]
    
    for test_case in test_cases:
        test_suite = unittest.TestSuite()
        test_suite.addTest(test_case)
        runner = unittest.TextTestRunner()
        runner.run(test_suite)