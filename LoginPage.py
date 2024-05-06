from BasePage import WebDriver
from selenium.webdriver.common.by import By

class LoginPage(WebDriver):
    
    def __init__(self):

        super().__init__()
    
   
    def Login(self,url,username,password):
        
        self.driver.get(url)
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "button").click()