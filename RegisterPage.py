from BasePage import WebDriver
from selenium.webdriver.common.by import By
import time

class RegisterPage(WebDriver):
    
    def __init__(self):

        super().__init__()
    
   
    def Register(self,url,fname,lname,address,city,state,zipn,phone,ssn,username,password,rpassword):
        
        self.driver.get(url)
        self.driver.find_element(By.ID, "customer.firstName").send_keys(fname)
        self.driver.find_element(By.NAME, "customer.lastName").send_keys(lname)
        self.driver.find_element(By.NAME, "customer.address.street").send_keys(address)
        self.driver.find_element(By.NAME, "customer.address.city").send_keys(city)
        self.driver.find_element(By.NAME, "customer.address.state").send_keys(state)
        self.driver.find_element(By.NAME, "customer.address.zipCode").send_keys(zipn)
        self.driver.find_element(By.NAME, "customer.phoneNumber").send_keys(phone)
        self.driver.find_element(By.NAME, "customer.ssn").send_keys(ssn)
        self.driver.find_element(By.NAME, "customer.username").send_keys(username)
        self.driver.find_element(By.NAME, "customer.password").send_keys(password)
        self.driver.find_element(By.NAME, "repeatedPassword").send_keys(rpassword)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[13]/td[2]/input").click()

        