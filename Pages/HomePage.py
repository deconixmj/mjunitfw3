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

    def click_icons(self,icon):
        icon1=""
        listoficons=HomePageLocators.iconlist
        # print(listoficons)
        # if icon in listoficons
        for i,j in listoficons:
            if icon in j:
                icon1=i,j
        # print(icon1)
        obj=HomePageLocators()
        action=ActionChains(self.driver)
        # x=getattr(obj,icon1)
        icon2=self.waitForElementVisibility(icon1)
        action.move_to_element(icon2).perform()
        icon2.click()
        # contactsicon.click()
        # y=HomePageLocators.contactsmenuitem
        # contactsmitem=self.waitForElementVisibility(y)
        # contactsmitem.click()
        # below action is not working as intended.
        action.release(icon2).perform()
        # action.perform()


        # self.driver.find_element(*HomePageLocators.contactsmenuitem).click()





