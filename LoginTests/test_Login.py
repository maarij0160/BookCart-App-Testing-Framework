from selenium.webdriver.common.by import By
import unittest
import time
from dotenv import load_dotenv, dotenv_values 
import sys
import os

load_dotenv() 
sys.path.insert(1, os.getenv("CONFIGPATH"))

from DriverConfig import WebDriver

class UnitTestsRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=WebDriver()

        cls.driver.initializeDriver()

    def test_validLogin(self):
        self.driver.driver.get(self.driver.url)
        username="Maarij1"
        password="temp123"
        self.driver.driver.find_element(By.CSS_SELECTOR, "#loginPanel .login .input").send_keys(username)
        self.driver.driver.find_elements(By.CSS_SELECTOR, "#loginPanel .login .input")[1].send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "#loginPanel .login .button").click()

        header = self.driver.driver.find_element(By.CSS_SELECTOR,"#rightPanel .title").text
        time.sleep(2)
        self.assertEqual(header,"Accounts Overview")

    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver

if __name__ == "__main__":
    unittest.main()
        