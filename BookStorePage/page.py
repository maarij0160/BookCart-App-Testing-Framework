from selenium.webdriver.common.by import By
class Page:

    # login
    def clickLoginLink(self,driver):
        driver.driver.find_element(By.CSS_SELECTOR, "[mattooltip='Login']").click()

    def enterUsernameField(self, driver, username):
        driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username)

    def enterPasswordField(self, driver, password):
        driver.driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Password']")[0].send_keys(password)

    def clickLoginButton(self,driver):
        driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()

    def getLoginHeader(self, driver):
        return driver.driver.find_element(By.CSS_SELECTOR,"a.mat-mdc-menu-trigger.mdc-button.mdc-button--unelevated.mat-mdc-unelevated-button.mat-primary.mat-mdc-button-base.ng-star-inserted").text
    
    def getInvalidLoginText(self,driver):
        return driver.driver.find_element(By.CSS_SELECTOR,"mat-error#mat-mdc-error-0.mat-mdc-form-field-error.mat-mdc-form-field-bottom-align").text
    

    # register
    def clickRegisterLink(self, driver):
        driver.driver.find_elements(By.CSS_SELECTOR,"button[tabindex='0']")[3].click()

    def enterFirstNameField(self, driver, firstName):
        driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='First name']").send_keys(firstName)

    def enterLastNameField(self, driver, lastName):
        driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']").send_keys(lastName)
    
    def enterRegUsernameField(self, driver, username):
        driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='User name']").send_keys(username)
    
    def enterRegPasswordField(self, driver, password):
        driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(password)
   
    def enterConfirmPasswordField(self, driver, confirmPassword):
        driver.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Confirm Password']").send_keys(confirmPassword)
    
    def clickGenderCheckbox(self, driver):
        driver.driver.find_element(By.CSS_SELECTOR, "mat-radio-button[value='Male']").click()
        
    def clickRegisterButton(self, driver):
        return driver.driver.find_element(By.CLASS_NAME, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base")[0]
    
    def getLoginTextBack(self,driver):
        return driver.driver.find_element(By.CSS_SELECTOR,"mat-card-title.mat-mdc-card-title.mat-h1").text