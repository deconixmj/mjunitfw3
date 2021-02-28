from Locators.Locator import SignInLocators,HomePageLocators,CalendarLocators,ContactsLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignIn:
    driver=""

    def __init__(self,d):
        self.driver=d

    def waitForElementVisibility(self, by):
        wait = WebDriverWait(self.driver, 20)
        return wait.until(EC.visibility_of_element_located(by))

    def click_signin(self):
        x=HomePageLocators.SIGNIN
        self.waitForElementVisibility(x).click()

    # login method
    def signin_user(self,username,password):
        # x=SignInLocators.Username
        # self.waitForElementVisibility(x).send_keys(username)
        # y=SignInLocators.password
        # self.waitForElementVisibility(y).send_keys(password)
        # z=SignInLocators.submit
        # self.waitForElementVisibility(z).click()
        self.driver.find_element(*SignInLocators.Username).send_keys(username)
        self.driver.find_element(*SignInLocators.Password).send_keys(password)
        self.driver.find_element(*SignInLocators.Submit).click()

    # validate user logged in
    def login_verify(self):
        x=HomePageLocators.loggedintext
        t=self.waitForElementVisibility(x).text
        # t=self.driver.find_element(*PostLoginLocators.loggedintext).text
        return t

    def validateHomePageTitle(self):
        return self.driver.gettitle()

    def ValidateCRMimage(self):
        pass





