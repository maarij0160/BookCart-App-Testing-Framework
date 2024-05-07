from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebDriver:
    
    def __init__(self) -> None:
        self.driver=None
        self.url="https://bookcart.azurewebsites.net/"

    def initializeDriver(self):    

        try:
            options = Options()
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            chromedriver = webdriver.Chrome(options=options)
            
            self.driver = chromedriver
            print("WebDriver initialized successfully!")    

        except Exception as e:
            print("Error initializing WebDriver:", e)

    
    def closeDriver(self):
        
        if self.driver:    
            self.driver.quit()
            print("WebDriver closed successfully!")



# driver= WebDriver()
# driver.initializeDriver()
# driver.closeDriver()