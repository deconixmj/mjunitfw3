from selenium import webdriver
from Locators.Locator import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Homepage:
    driver=""

    def __init__(self,d):
        self.driver=d

    def waitForElementVisibility(self,by):
        wait=WebDriverWait(self.driver,20)
        return wait.until(EC.visibility_of_element_located(by))

    def click_sign_up(self):
        x=HomePageLocators.SIGNUP
        self.waitForElementVisibility(x).click()
        # self.driver.find_element(*HomePageLocators.SIGNUP).click()

    def click_contacts(self):
        action=ActionChains(self.driver)
        x=HomePageLocators.Contactsicon
        contactsicon=self.waitForElementVisibility(x)
        action.move_to_element(contactsicon).perform()
        # contactsicon.click()
        y=HomePageLocators.contactsmenuitem
        contactsmitem=self.waitForElementVisibility(y)
        contactsmitem.click()
        # below action is not working as intended.
        action.release(contactsmitem).perform()
        # action.perform()


        # self.driver.find_element(*HomePageLocators.contactsmenuitem).click()





