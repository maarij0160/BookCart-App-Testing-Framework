from config import WebDriver
from selenium.webdriver.common.by import By
import unittest
import time

class UnitTestsRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=WebDriver()

        cls.driver.initializeDriver()

    def test_validLogin(self):
        self.driver.driver.get(self.driver.url)
        username="FaheemTest"
        password="temp123"
        self.driver.driver.find_element(By.CSS_SELECTOR, "#loginPanel .login .input").send_keys(username)
        self.driver.driver.find_elements(By.CSS_SELECTOR, "#loginPanel .login .input")[1].send_keys(password)
        self.driver.driver.find_element(By.CSS_SELECTOR, "#loginPanel .login .button").click()

        header = self.driver.driver.find_element(By.CSS_SELECTOR,"#rightPanel .title").text
        time.sleep(2)
        self.assertEqual(header,f"Welcome {username}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver

if __name__ == "__main__":
    unittest.main()
        