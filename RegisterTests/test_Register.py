import sys
import os
from dotenv import load_dotenv

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
    def setUpClass(cls):
        cls.driver=WebDriver()

        cls.driver.initializeDriver()

        
    def test_01_validRegister(self):
        self.driver.driver.get(self.driver.url)
        firstName="Muhammad"
        lastName="Faheem"
        username="Maarij697789012"
        password="Temp123456"
        
        registerPage= Page()
        
        registerPage.clickLoginLink(self.driver)
        registerPage.clickRegisterLink(self.driver)
        registerPage.enterFirstNameField(self.driver, firstName)
        registerPage.enterLastNameField(self.driver, lastName)
        registerPage.enterRegUsernameField(self.driver, username)
        registerPage.enterRegPasswordField(self.driver, password)
        registerPage.enterConfirmPasswordField(self.driver, password)
        registerPage.clickGenderCheckbox(self.driver)
        
        time.sleep(5)
        registerPage.clickRegisterButton(self.driver)
        time.sleep(5)
        header= registerPage.getLoginTextBack(self.driver)
        self.assertEqual(header,'Login')

    
    def test_02_InvalidRegister(self):
        
        self.driver.driver.get(self.driver.url)
        firstName="Muhammad"
        lastName="Faheem"
        username="Maarij697789012"
        password="Temp123456"

        registerPage= Page()
        
        registerPage.clickLoginLink(self.driver)
        registerPage.clickRegisterLink(self.driver)
        registerPage.enterFirstNameField(self.driver, firstName)
        registerPage.enterLastNameField(self.driver, lastName)
        registerPage.enterRegUsernameField(self.driver, username)
        registerPage.enterRegPasswordField(self.driver, password)
        registerPage.enterConfirmPasswordField(self.driver, password)
        registerPage.clickGenderCheckbox(self.driver)

        
        time.sleep(5)
        
        try:
            reg_button = registerPage.clickRegisterButton(self.driver)
            if reg_button.is_enabled():
                reg_button.click()
        except:
            pass
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver()

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(UnitTestsRegister('test_01_validRegister'))
    test_suite.addTest(UnitTestsRegister('test_02_InvalidRegister'))
    
    unittest.TextTestRunner().run(test_suite)
    
        