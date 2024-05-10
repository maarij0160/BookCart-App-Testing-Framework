from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        return driver.driver.find_element(By.XPATH,"/html/body/app-root/div/app-login/div/mat-card/mat-card-header/div[1]/mat-card-title").text
    
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
        return driver.driver.find_element(By.XPATH, "/html/body/app-root/div/app-user-registration/div/mat-card/mat-card-content/form/mat-card-actions/button")
    
    def getLoginTextBack(self,driver):
        return driver.driver.find_element(By.CSS_SELECTOR,"mat-card-title.mat-mdc-card-title.mat-h1").text


    #category
    def clickBiography(self,driver):
        return WebDriverWait(driver.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-home/div/div[1]/div/app-book-filter/mat-nav-list/mat-list-item[2]"))
        )

    def clickFiction(self,driver):
        return WebDriverWait(driver.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-home/div/div[1]/div/app-book-filter/mat-nav-list/mat-list-item[3]"))
        )

    def clickMystery(self,driver):
        return WebDriverWait(driver.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-home/div/div[1]/div/app-book-filter/mat-nav-list/mat-list-item[4]"))
        )    

    def clickFantasy(self,driver):
        return WebDriverWait(driver.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-home/div/div[1]/div/app-book-filter/mat-nav-list/mat-list-item[5]"))
        )     

    def clickRomance(self,driver):
        return WebDriverWait(driver.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-home/div/div[1]/div/app-book-filter/mat-nav-list/mat-list-item[6]"))
        )

    def clickBook(self,driver):
        driver.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div/div[2]/div/div[1]/app-book-card/mat-card/a").click()

    def getBookCategory(self,driver):
        return driver.driver.find_element(By.XPATH, "/html/body/app-root/div/app-book-details/mat-card/mat-card-content/div[2]/table/tbody/tr[3]/td[2]")    


    #search
    
    def giveInput(self,driver):
        return WebDriverWait(driver.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-nav-bar/mat-toolbar/mat-toolbar-row/div[2]/app-search/form/input"))
        )
        
    def getBookName(self,driver):
        return driver.driver.find_element(By.XPATH, "/html/body/app-root/div/app-book-details/mat-card/mat-card-content/div[2]/table/tbody/tr[1]/td[2]")
    
    
    #cart
    
    def getCartCount(self,driver):
        return driver.driver.find_elements(By.CSS_SELECTOR, "span#mat-badge-content-0.mat-badge-content.mat-badge-active")[0].text
    
    def addItemToCart(self,driver):
        driver.driver.find_element(By.CSS_SELECTOR, "button.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base").click()
        
        
    def goToCart(self,driver):
        driver.driver.find_elements(By.CSS_SELECTOR,"button[tabindex='0']")[2].click()
        
    def IncQty(self,driver):
        driver.driver.find_element(By.CSS_SELECTOR,"td.mat-mdc-cell.mat-column-quantity > div > div:nth-child(3) > button").click()
        
        
    def DecQty(self,driver):
        driver.driver.find_element(By.CSS_SELECTOR,"td.mat-mdc-cell.mat-column-quantity > div > div:nth-child(1) > button").click()
        
    
    def getItemCount(self,driver):
        return driver.driver.find_element(By.CSS_SELECTOR, "div.d-flex.align-items-center > div:nth-child(2)").text
    
    def deleteItem(self,driver):
        driver.driver.find_element(By.CSS_SELECTOR,"body > app-root > div > app-shoppingcart > mat-card > mat-card-content.mat-mdc-card-content.my-3.ng-star-inserted > table > tbody > tr > td.mat-mdc-cell.mdc-data-table__cell.cdk-cell.cdk-column-action.mat-column-action.ng-star-inserted > button").click()
        
    def clearCart(self,driver):
        driver.driver.find_elements(By.CSS_SELECTOR,"body > app-root > div > app-shoppingcart > mat-card > mat-card-header > div.ng-star-inserted > button")[0].click()
        
        
    #wishlist
    
    def getWishlistCount(self,driver):
        return driver.driver.find_element(By.CSS_SELECTOR, "body > app-root > app-nav-bar > mat-toolbar > mat-toolbar-row > div.d-flex.align-items-center > button.mdc-icon-button.mat-mdc-icon-button.mat-unthemed.mat-mdc-button-base.ng-star-inserted").text
    
    def addToWishlist(self,driver):
        driver.driver.find_element(By.CSS_SELECTOR, "body > app-root > div > app-home > div > div.col.mb-3 > div > div:nth-child(1) > app-book-card > mat-card > mat-card-content > div.favourite.mat-elevation-z8.ng-star-inserted > app-addtowishlist > span").click()
        
    def removeFromList(self,driver):
        driver.driver.find_element(By.CSS_SELECTOR,"body > app-root > div > app-home > div > div.col.mb-3 > div > div:nth-child(1) > app-book-card > mat-card > mat-card-content > div.favourite.mat-elevation-z8.ng-star-inserted > app-addtowishlist > span").click()
        
    def goToWishlist(self,driver):
        driver.driver.find_elements(By.CSS_SELECTOR,"button[tabindex='0']")[1].click()
        
    def clearWishlist(self,driver):
        driver.driver.find_element(By.CSS_SELECTOR,"button.mat-elevation-z4.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-unthemed.mat-mdc-button-base").click()