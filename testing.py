from BasePage import WebDriver
from LoginPage import LoginPage
from selenium.webdriver.common.by import By


def LoginWithValidUser():
    
    WebDriver.initialize_driver()
    
    login = LoginPage()
    login.Login("https://adactinhotelapp.com/","AmirTester","AmirTester")
    
    
    welcome_message = WebDriver.driver.find_element(By.CLASS_NAME, "welcome_menu").text
    
    assert welcome_message == "Welcome to Adactin Group of Hotels"
    
    print("Valid Login Test Passed")
    
    WebDriver.close_driver()



def LoginWithInvalidUser():
    
    WebDriver.initialize_driver()
    
    login = LoginPage()
    login.Login("https://adactinhotelapp.com/","AmirTester","AmirTester123")
    
    
    welcome_message = WebDriver.driver.find_element(By.CLASS_NAME, "auth_error").text
    
    assert welcome_message == "Invalid Login details or Your Password might have expired. Click here to reset your password"
    
    print("InValid Login Test Passed")
    
    WebDriver.driver.quit()

LoginWithValidUser()
LoginWithInvalidUser()