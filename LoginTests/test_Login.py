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


class UnitTestsLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver()

        cls.driver.initializeDriver()

    def test_validLogin(self):
        self.driver.driver.get(self.driver.url)
        username = "hello"
        password = "hello123"
        loginPage = Page()

        
        loginPage.clickLoginLink(self.driver)
        loginPage.enterUsernameField(self.driver, username)
        loginPage.enterPasswordField(self.driver, password)
        loginPage.clickLoginButton(self.driver)
        time.sleep(2)
        header = loginPage.getLoginHeader(self.driver)
        header = header.split("\n")[-1]
        self.assertEqual(header, username)

    def test_InvalidLogin(self):

        self.driver.driver.get(self.driver.url)
        username = "hello"
        password = "hello"
        loginPage = Page()

        loginPage.clickLoginLink(self.driver)
        loginPage.enterUsernameField(self.driver, username)
        loginPage.enterPasswordField(self.driver, password)
        loginPage.clickLoginButton(self.driver)
        time.sleep(2)
        text = loginPage.getInvalidLoginText(self.driver)
        self.assertEqual(text, "Username or Password is incorrect.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver


if __name__ == "__main__":
    unittest.main()
