from Locators.Locator import HomePageLocators,ContactsLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class ContactsPage:
    driver=""
    def __init__(self,d):
        self.driver=d

    def waitForElementVisibility(self,by):
        wait=WebDriverWait(self.driver,20)
        return wait.until(EC.visibility_of_element_located(by))

    def validateContactsPageLabel(self):
        t=HomePageLocators.contactslabel
        t1=self.waitForElementVisibility(t).text
        return t1


    def createnewcontact(self):
        self.driver.find_element(*ContactsLocators.contactnew).click()
        time.sleep(5)
        self.driver.find_element(*ContactsLocators.fname).send_keys("bipul")
        self.driver.find_element(*ContactsLocators.lname).send_keys("talukdar")
        self.driver.find_element(*ContactsLocators.comp).send_keys("tcs")
        time.sleep(3)
        opt=self.driver.find_element(*ContactsLocators.comp_search)
        for i in opt:
            if i.text=="tcs":
                i.click()

        self.driver.find_element(*ContactsLocators.save).click()
