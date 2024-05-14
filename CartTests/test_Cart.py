from selenium.webdriver.common.by import By
import unittest
import time
import pandas as pd
df=pd.read_csv('CartTests/carts.csv')
from dotenv import load_dotenv
import sys
import os

load_dotenv() 
sys.path.insert(1, os.getenv("CONFIGPATH"))

from DriverConfig import WebDriver
sys.path.insert(1, os.getenv("CONFIGBOOK"))
from page import Page


class UnitTestsCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=WebDriver()

        cls.driver.initializeDriver()

    def test_addtocart(self):
        
        self.driver.driver.get(self.driver.url)
        username=df.iloc[0,0]
        password=df.iloc[0,1]
        
        cart = Page()
        
        self.driver.driver.get("https://bookcart.azurewebsites.net/login")

        time.sleep(2)

        cart.enterUsernameField(self.driver, username)
        cart.enterPasswordField(self.driver, password)
        cart.clickLoginButton(self.driver)
        time.sleep(2)
       
        initial = cart.getCartCount(self.driver)
        cart.addItemToCart(self.driver)
       
        
        time.sleep(2)
       
        final = cart.getCartCount(self.driver)
        self.assertEqual(int(initial) + 1,int(final))
      
        
    
        
    def test_incQty(self):
        
        self.driver.driver.get(self.driver.url)
        username=df.iloc[0,0]
        password=df.iloc[0,1]
        
        cart = Page()
        
        self.driver.driver.get("https://bookcart.azurewebsites.net/login")

        time.sleep(2)

        cart.enterUsernameField(self.driver, username)
        cart.enterPasswordField(self.driver, password)
        cart.clickLoginButton(self.driver)
        time.sleep(2)
        
        cart.addItemToCart(self.driver)
        time.sleep(2)
        
        cart.goToCart(self.driver)
        
        time.sleep(2)
       
        initial = cart.getCartCount(self.driver)
        cart.IncQty(self.driver)
        
        time.sleep(2)
        final = cart.getCartCount(self.driver)
       
        time.sleep(2)
        self.assertEqual(int(initial) + 1,int(final))
        
        
    def test_decQty(self):
        
        self.driver.driver.get(self.driver.url)
        username=df.iloc[0,0]
        password=df.iloc[0,1] 
        
        cart = Page()
        
        self.driver.driver.get("https://bookcart.azurewebsites.net/login")

        time.sleep(2)

        cart.enterUsernameField(self.driver, username)
        cart.enterPasswordField(self.driver, password)
        cart.clickLoginButton(self.driver)
        time.sleep(2)
        
        
        cart.addItemToCart(self.driver)
        time.sleep(2)
        cart.goToCart(self.driver)
        
        time.sleep(2)
       
        initial = cart.getCartCount(self.driver)
        cart.DecQty(self.driver)
        
        time.sleep(2)
        final = cart.getCartCount(self.driver)
       
        time.sleep(2)
        
        self.assertEqual(int(initial) - 1,int(final))

        
    def test_deleteItem(self):
        
            
        self.driver.driver.get(self.driver.url)
        username=df.iloc[0,0]
        password=df.iloc[0,1]
        
        cart = Page()
        
        self.driver.driver.get("https://bookcart.azurewebsites.net/login")

        time.sleep(2)

        cart.enterUsernameField(self.driver, username)
        cart.enterPasswordField(self.driver, password)
        cart.clickLoginButton(self.driver)
        time.sleep(2)
        
        cart.addItemToCart(self.driver)
        
        time.sleep(2)
        cart.goToCart(self.driver)
        
        time.sleep(2)
        initialcart = cart.getCartCount(self.driver)
        itemcount = cart.getItemCount(self.driver)
       
        cart.deleteItem(self.driver)
        time.sleep(2)
        final = cart.getCartCount(self.driver)
        
        time.sleep(2)
        self.assertEqual(int(initialcart) - int(itemcount),int(final))

            
    def test_clearcart(self):
        
        self.driver.driver.get(self.driver.url)
        username=df.iloc[0,0]
        password=df.iloc[0,1]
        
        cart = Page()
        
        self.driver.driver.get("https://bookcart.azurewebsites.net/login")

        time.sleep(2)

        cart.enterUsernameField(self.driver, username)
        cart.enterPasswordField(self.driver, password)
        cart.clickLoginButton(self.driver)
        time.sleep(2)
        
        cart.addItemToCart(self.driver)
        
        time.sleep(2)
        cart.goToCart(self.driver)
        
        time.sleep(2)
        cart.clearCart(self.driver)
        
        time.sleep(2)
        final = cart.getCartCount(self.driver)
        
        self.assertEqual(int(final),0)
   
        
    
     
    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver

if __name__ == "__main__":
    unittest.main()
    
    
    
    