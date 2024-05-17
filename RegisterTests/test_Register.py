import sys
import os
from dotenv import load_dotenv
import pandas as pd

df = pd.read_csv("RegisterTests/register.csv")

load_dotenv()
sys.path.insert(1, os.getenv("CONFIGPATH"))


from DriverConfig import WebDriver

sys.path.insert(1, os.getenv("CONFIGBOOK"))
from page import Page
from selenium.webdriver.common.by import By
import unittest
import time


class UnitTestsRegister(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = WebDriver()

        cls.driver.initializeDriver()

    def test_InvalidRegister(self):

        self.driver.driver.get(self.driver.url)
        firstName = df.iloc[0, 0]
        lastName = df.iloc[0, 1]
        username = df.iloc[0, 2]
        password = df.iloc[0, 3]

        register = Page()

        register.clickLoginLink(self.driver)
        register.clickRegisterLink(self.driver)

        time.sleep(2)
        register.enterFirstNameField(self.driver, firstName)

        register.enterLastNameField(self.driver, lastName)

        register.enterRegUsernameField(self.driver, username)
        register.enterRegPasswordField(self.driver, password)
        register.enterConfirmPasswordField(self.driver, password)
        time.sleep(2)
        register.clickGenderCheckbox(self.driver)
        time.sleep(5)

        try:
            reg_button = register.clickRegisterButton(self.driver)
            if reg_button.is_enabled():
                reg_button.click()
        except:
            pass

        self.driver.closeDriver()

    def test_validRegister(self):

        self.driver.driver.get(self.driver.url)
        firstName = df.iloc[10, 0]
        lastName = df.iloc[10, 1]
        username = df.iloc[10, 2]
        password = df.iloc[10, 3]

        register = Page()

        register.clickLoginLink(self.driver)
        register.clickRegisterLink(self.driver)

        time.sleep(2)
        register.enterFirstNameField(self.driver, firstName)

        register.enterLastNameField(self.driver, lastName)

        register.enterRegUsernameField(self.driver, username)
        register.enterRegPasswordField(self.driver, password)
        register.enterConfirmPasswordField(self.driver, password)
        time.sleep(2)
        register.clickGenderCheckbox(self.driver)

        time.sleep(15)
        reg_button = register.clickRegisterButton(self.driver)
        reg_button.click()
        time.sleep(5)
        header = register.getLoginTextBack(self.driver)
        self.assertEqual(header, "Login")

    @classmethod
    def tearDown(cls):
        cls.driver.closeDriver()


if __name__ == "__main__":
    unittest.main()
