from selenium.webdriver.common.by import By
import unittest
import time
from dotenv import load_dotenv
import pandas as pd
df=pd.read_csv('WishListTests/wishlist.csv')
import sys
import os

load_dotenv() 
sys.path.insert(1, os.getenv("CONFIGPATH"))

from DriverConfig import WebDriver
sys.path.insert(1, os.getenv("CONFIGBOOK"))
from page import Page

class UnitTestsWishList(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver=WebDriver()

        cls.driver.initializeDriver()

    def test_addtoList(self):
        
        print('here')
        self.driver.driver.get(self.driver.url)
        username=df.iloc[0,0]
        password=df.iloc[0,1]
        
        wishlist = Page()
        wishlist.clickLoginLink(self.driver)
        wishlist.enterUsernameField(self.driver, username)
        wishlist.enterPasswordField(self.driver, password)
        wishlist.clickLoginButton(self.driver)
        time.sleep(2)
        
        initial = wishlist.getWishlistCount(self.driver)
        
        
        wishlist.addToWishlist(self.driver)
        
        
        time.sleep(2)
        
        final = wishlist.getWishlistCount(self.driver)
        initial = initial.split("\n")[-1]
        final = final.split("\n")[-1]
        self.assertEqual(int(initial) + 1,int(final))
        
    def test_removefromList(self):
        
        self.driver.driver.get(self.driver.url)
        username=df.iloc[0,0]
        password=df.iloc[0,1]
        
        wishlist = Page()
        wishlist.clickLoginLink(self.driver)
        wishlist.enterUsernameField(self.driver, username)
        wishlist.enterPasswordField(self.driver, password)
        wishlist.clickLoginButton(self.driver)
        time.sleep(2)
        
        
        initial = wishlist.getWishlistCount(self.driver)
        
        wishlist.removeFromList(self.driver)
        
        
        time.sleep(2)
        
        final = wishlist.getWishlistCount(self.driver)
        
        initial = initial.split("\n")[-1]
        final = final.split("\n")[-1]
        self.assertEqual(int(initial) - 1,int(final))
        
        
    def test_clearList(self):
        
        self.driver.driver.get(self.driver.url)
        username=df.iloc[0,0]
        password=df.iloc[0,1] 
        
        wishlist = Page()
        wishlist.clickLoginLink(self.driver)
        wishlist.enterUsernameField(self.driver, username)
        wishlist.enterPasswordField(self.driver, password)
        wishlist.clickLoginButton(self.driver)
        time.sleep(2)
        
        wishlist.addToWishlist(self.driver)
        
        
        time.sleep(2)
        wishlist.goToWishlist(self.driver)
        
        
        time.sleep(2)
        wishlist.clearWishlist(self.driver)
        
        time.sleep(2)
        final = wishlist.getWishlistCount(self.driver)
        final = final.split("\n")[-1]
        self.assertEqual(int(final),0)
        
     
    @classmethod
    def tearDown(cls):
        cls.driver.closeDriver

if __name__ == "__main__":
    unittest.main()
    