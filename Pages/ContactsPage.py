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


    def createnewcontact(self,fname,lname,company):
        self.driver.find_element(*ContactsLocators.contactnew).click()
        time.sleep(5)
        self.driver.find_element(*ContactsLocators.fname).send_keys(fname)
        self.driver.find_element(*ContactsLocators.lname).send_keys(lname)
        self.driver.find_element(*ContactsLocators.comp).send_keys(company)
        time.sleep(3)
        s=self.driver.find_elements(*ContactsLocators.comp_search)
        if len(s) == 1:
            s[0].click()
        else:
            for x in range(len(s)):
                if s[x].text == company:
                    s[x].click()

        self.driver.find_element(*ContactsLocators.save).click()
        time.sleep(3)

        contact_name = fname + " " + lname
        xpath1 = '//div[text()="{}"]'.format(contact_name)
        name=self.driver.find_element_by_xpath(xpath1).text
        return name

    # def delete_contact(self):

