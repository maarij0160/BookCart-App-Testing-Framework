from selenium.webdriver.common.by import By
import unittest
import time
from dotenv import load_dotenv
import sys
import os
from selenium.webdriver.common.keys import Keys

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

        time.sleep(3)
        loginPage.clickLoginLink(self.driver)
        loginPage.enterUsernameField(self.driver, username)
        loginPage.enterPasswordField(self.driver, password)
        loginPage.clickLoginButton(self.driver)
        time.sleep(3)
        header = loginPage.getLoginHeader(self.driver)
        header = header.split("\n")[-1]
        self.assertEqual(header, username)

    def test_InvalidLogin(self):

        self.driver.driver.get(self.driver.url)
        username = "hello"
        password = "hello"
        loginPage = Page()

        self.driver.driver.get("https://bookcart.azurewebsites.net/login")

        time.sleep(2)
        
        loginPage.enterUsernameField(self.driver, username)
        loginPage.enterPasswordField(self.driver, password)
        time.sleep(2)
        loginPage.clickLoginButton(self.driver)
        time.sleep(2)
        text = loginPage.getInvalidLoginText(self.driver)
        self.assertEqual(text, "Username or Password is incorrect.")
        self.driver.closeDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver


if __name__ == "__main__":
    unittest.main()
