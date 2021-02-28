from selenium.webdriver.common.by import By

class HomePageLocators:
    #SIGNUP=(By.LINK_TEXT,'sign up')
    SIGNUP=(By.XPATH,'(//a[@href="https://register.freecrm.com/register/"])')
    SIGNIN=(By.XPATH,"(//span[contains(text(),'Log In')])")
    loggedintext = (By.XPATH, "(//span[contains(text(),'Mj P')])")
    crmlogo=None
    Calendaricon=(By.XPATH,'//i[@xpath=1]')
    Contactsicon=(By.XPATH,'//i[@class="users icon"]')
    contactsmenuitem=(By.XPATH,'//span[contains(text(),"Contacts")]')
    contactslabel=(By.XPATH,'//div[text()="Contacts"]')


class SignUPLocators:
    Email=(By.ID,'email')
    Phone=(By.NAME,'phone')
    Terms=(By.ID,'terms')
    captcha=(By.XPATH,'//*[@id="recaptcha-anchor"]/div[1]')
    Submit=(By.NAME,'action')
    Error_email=(By.XPATH,'//div[@class="ui negative message"]/ul/li[1]')
    Error_phone=(By.XPATH,'//div[@class="ui negative message"]/ul/li[2]')
    Error_termscheckbox=(By.XPATH,'//div[@class="ui negative message"]/ul/li[3]')
    Error_captcha=(By.XPATH,'//div[@class="ui negative message"]/ul/li[4]')


class SignInLocators:
    Username=(By.NAME,'email')
    Password=(By.NAME,'password')
    Submit=(By.XPATH,'(//div[contains(text(),"Login")])[1]')

class CalendarLocators:
    pass

class ContactsLocators:
    contactnew=(By.XPATH,'//button[text()="New"]')
    fname=(By.NAME,'first_name')
    lname=(By.NAME,'last_name')
    comp=(By.XPATH,'//input[@class="search"]')
    comp_search=(By.XPATH,'//div[@class="visible menu transition"]/div/span')
    save=(By.XPATH,'//button[text()="Save"]')


class CompaniesLocators:
    pass

class DealsLocators:
    pass

class TasksLocators:
    pass
