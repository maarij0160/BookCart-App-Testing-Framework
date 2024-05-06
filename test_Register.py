from config import WebDriver
from selenium.webdriver.common.by import By
import unittest
import time

class UnitTestsRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=WebDriver()

        cls.driver.initializeDriver()

    def test_validRegister(self):
        self.driver.driver.get(self.driver.url)
        firstName="Muhammad"
        lastName="Faheem"
        street="ABC"
        city="Karachi"
        state="Sindh"
        zipCode="76324"
        phoneNumber="0213243254"
        ssn="ABC-123"
        username="FaheemTest2"
        password="temp123"
        time.sleep(3)
        print(self.driver.driver.find_elements(By.CSS_SELECTOR, "#loginPanel p a")[1].click())
        time.sleep(3)
        self.driver.driver.find_element(By.ID, "customer\.firstName").send_keys(firstName)
        
        self.driver.driver.find_element(By.ID, "customer\.lastName").send_keys(lastName)
        self.driver.driver.find_element(By.ID, "customer\.address.street").send_keys(street)
        self.driver.driver.find_element(By.ID, "customer\.address.city").send_keys(city)
        self.driver.driver.find_element(By.ID, "customer\.address.state").send_keys(state)
        self.driver.driver.find_element(By.ID, "customer\.address.zipCode").send_keys(zipCode)
        self.driver.driver.find_element(By.ID, "customer\.phoneNumber").send_keys(phoneNumber)
        self.driver.driver.find_element(By.ID, "customer\.ssn").send_keys(ssn)
        self.driver.driver.find_element(By.ID, "customer\.username").send_keys(username)
        self.driver.driver.find_element(By.ID, "customer\.password").send_keys(password)
        self.driver.driver.find_element(By.ID, "repeatedPassword").send_keys(password)
        
        self.driver.driver.find_element(By.CSS_SELECTOR, "#customerForm .form2 tbody tr td .button").click()
        time.sleep(2)
        header = self.driver.driver.find_element(By.CSS_SELECTOR,"#rightPanel .title").text
        self.assertEqual(header,f"Welcome {username}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.closeDriver()

if __name__ == "__main__":
    unittest.main()
        