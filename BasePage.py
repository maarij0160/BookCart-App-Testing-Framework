from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebDriver:
    driver = None

    @staticmethod
    def initialize_driver():
        
        try:
            options = Options()
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            chromedriver = webdriver.Chrome(options=options)
            
            WebDriver.driver = chromedriver
            print("WebDriver initialized successfully!")
            
        except Exception as e:
            print("Error initializing WebDriver:", e)

    @staticmethod
    def close_driver():
        
        if WebDriver.driver:
            
            WebDriver.driver.quit()
            print("WebDriver closed successfully!")