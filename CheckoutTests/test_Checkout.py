from selenium.webdriver.common.by import By
import unittest
import time
import pandas as pd
df=pd.read_csv('CheckoutTests/checkout.csv')
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
        username=df.iloc[0,0]
        password=df.iloc[0,1] 
        name = df.iloc[0,2]
        address1 = df.iloc[0,3]
        address2 = df.iloc[0,4]
        pincode = df.iloc[0,5]
        state = df.iloc[0,6]
        
        checkout = Page()
        
        self.driver.driver.get("https://bookcart.azurewebsites.net/login")
        checkout.enterUsernameField(self.driver, username)
        checkout.enterPasswordField(self.driver, password)
        checkout.clickLoginButton(self.driver)
        time.sleep(2)
        
        checkout.addItemToCart(self.driver)
        
        
        time.sleep(2)
        
        
        checkout.goToCart(self.driver)
        time.sleep(4)
        checkout.clickCheckoutButton(self.driver)
        
        
        time.sleep(2)
        
        checkout.enterName(self.driver, name)
        checkout.enterAddress1(self.driver, address1)
        checkout.enterAddress2(self.driver, address2)
        checkout.enterPincode(self.driver, pincode)
        checkout.enterState(self.driver, state)
        
        time.sleep(4)
        checkout.clickPlaceOrderButton(self.driver)
        
        time.sleep(10)
        
        final = checkout.getCartCount(self.driver)
        time.sleep(2)
        self.assertEqual(int(final),0)
        self.driver.closeDriver()
     
    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver

if __name__ == "__main__":
    unittest.main()
        