from Locators.Locator import HomePageLocators,DealsLocators
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class DealsPage:

    driver=""
    def __init__(self,d):
        self.driver=d

    def waitForElementVisibility(self,by):
        wait=WebDriverWait(self.driver,10)
        return wait.until(EC.visibility_of_element_located(by))


    def verify_dealspagelabel(self):

        t = DealsLocators.dealslabel
        t1 = self.waitForElementVisibility(t).text
        return t1
        # t=self.driver.find_element(*).text
        # return t


    def validate_newdeal(self,title,stage,status):

        d=DealsLocators.dealsnew
        self.waitForElementVisibility(d).click()

        # self.driver.find_element(*DealsLocators.dealsnew).click()
        time.sleep(3)

        self.driver.find_element(*DealsLocators.title1).send_keys(title)


        # Y=1080
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        s1=self.driver.find_elements(*DealsLocators.stageL)
        s1[0].click()
        # self.driver.find_element(*DealsLocators.stage1).click()
        # self.driver.
        # print(s1)
        for i in range(len(s1)):
            if s1[i].text==stage:
                s1[i].click()
                break


        # s2=Select(s1)
        # s2.select_by_visible_text(stage)
        st1=self.driver.find_elements(*DealsLocators.statusL)
        st1[0].click()
        for i in range(len(st1)):
            if st1[i].text==status:
                st1[i].click()
                break

        # st2=Select(st1)
        # st2.select_by_visible_text(status)
        # self.driver.find_element(*DealsLocators.public_toggle).click()


        time.sleep(3)
        # st3 = self.driver.find_element_by_xpath('//i[@class="lock icon"]').get_attribute('class')

        self.driver.find_element(*DealsLocators.save).click()
        time.sleep(3)

        #creating xpath locator value using format specifier
        t_xpath='//div[text()="{}"]'.format(title)
        t=self.driver.find_element_by_xpath(t_xpath)
        return t




        # t=DealsLocators.title
        # self.waitForElementVisibility(t).send_keys(title)
        # s1=DealsLocators.stageL
        # s2=Select(self.waitForElementVisibility(s1))
        # s2.select_by_visible_text(stage)
        # st1=DealsLocators.statusL
        # st2=Select(self.waitForElementVisibility(st1))
        # st2.select_by_visible_text(status)
        # ptoggle=DealsLocators.public_toggle









