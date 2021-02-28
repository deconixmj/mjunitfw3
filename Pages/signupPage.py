from Locators.Locator import SignUPLocators

class Signup:

    driver=""
    def __init__(self,d):
        self.driver=d

    def register_user(self,email,phone):
        self.driver.find_element(*SignUPLocators.Email).send_keys(email)
        self.driver.find_element(*SignUPLocators.Phone).send_keys(phone)
        self.driver.find_element(*SignUPLocators.Terms).click()
        self.driver.find_element(*SignUPLocators.captcha).click()
        self.driver.find_element(*SignUPLocators.Submit).click()

    def register_user_without_signup_err(self):
        self.driver.find_element(*SignUPLocators.Submit).click()

        self.error_email=self.driver.find_element(*SignUPLocators.Error_email).text
        self.error_phone = self.driver.find_element(*SignUPLocators.Error_phone).text
        self.error_terms = self.driver.find_element(*SignUPLocators.Error_termscheckbox).text
        self.error_captcha = self.driver.find_element(*SignUPLocators.Error_captcha).text

        return self.error_email,self.error_phone,self.error_terms, self.error_captcha

