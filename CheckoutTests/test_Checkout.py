from selenium.webdriver.common.by import By
import unittest
import time
from dotenv import load_dotenv
import sys
import os

load_dotenv() 
sys.path.insert(1, os.getenv("CONFIGPATH"))

from DriverConfig import WebDriver

sys.path.insert(1, os.getenv("CONFIGBOOK"))
from page import Page

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
        
        checkout = Page()
        
        checkout.clickLoginLink(self.driver)
        checkout.enterUsernameField(self.driver, username)
        checkout.enterPasswordField(self.driver, password)
        checkout.clickLoginButton(self.driver)
        time.sleep(2)
        
        checkout.addItemToCart(self.driver)
        
        
        time.sleep(2)
        
        
        checkout.goToCart(self.driver)
        time.sleep(2)
        checkout.clickCheckoutButton(self.driver)
        
        
        time.sleep(2)
        
        checkout.enterName(self.driver, name)
        checkout.enterAddress1(self.driver, address1)
        checkout.enterAddress2(self.driver, address2)
        checkout.enterPincode(self.driver, pincode)
        checkout.enterState(self.driver, state)
        
        time.sleep(2)
        checkout.clickPlaceOrderButton(self.driver)
        
        time.sleep(7)
        
        final = checkout.getCartCount(self.driver)
        time.sleep(2)
        self.assertEqual(int(final),0)
     
    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver

if __name__ == "__main__":
    unittest.main()
        