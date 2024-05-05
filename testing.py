from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep



def LoginTest(driver):
    
    
    driver.get("https://adactinhotelapp.com/")
    driver.find_element(By.ID, "username").send_keys("AmirTester")
    driver.find_element(By.ID, "password").send_keys("AmirTester")
    driver.find_element(By.ID, "login").click()
    
    welcome_message = driver.find_element(By.CLASS_NAME, "welcome_menu").text
    
    assert welcome_message == "Welcome to Adactin Group of Hotels"
    
    print("LoginTest Passed")
    
    driver.quit()




options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
LoginTest(driver)
