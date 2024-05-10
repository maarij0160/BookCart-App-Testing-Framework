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

class UnitTestsWishList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=WebDriver()

        cls.driver.initializeDriver()

    def test_addtoList(self):
        
        print('here')
        self.driver.driver.get(self.driver.url)
        username="hello"
        password="hello123" 
        
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
        username="hello"
        password="hello123" 
        
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
        username="hello"
        password="hello123" 
        
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
    def tearDownClass(cls):
        cls.driver.closeDriver

if __name__ == "__main__":
    
    #unittest.main()
    testcase = test_cases = [UnitTestsWishList('test_addtoList'), 
                  UnitTestsWishList('test_removefromList'), 
                  UnitTestsWishList('test_clearList')]
    
    
    for test_case in testcase:
        test_suite = unittest.TestSuite()
        test_suite.addTest(test_case)
        runner = unittest.TextTestRunner()
        runner.run(test_suite)