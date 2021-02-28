import unittest
import time
from selenium import webdriver
from Pages.BasePage import Basepage
from Pages.HomePage import Homepage
from Pages.SigninPage import SignIn
from Pages.ContactsPage import ContactsPage
# from Pages.signupPage import Signup
from ddt import ddt,data,idata,unpack
from Testdata.readdata import getdata_signin

@ddt
class TestNewContact(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        url = "https://freecrm.com/"
        cls.base = Basepage(url)
        cls.home = Homepage(cls.base.driver)
        cls.signin1 = SignIn(cls.base.driver)

        cls.signin1.click_signin()
        cls.home1 = Homepage(cls.base.driver)
        cls.contact = ContactsPage(cls.base.driver)

    def setUp(self):
        # self.contactshome=Homepage(self.base.driver)
        L=getdata_signin()
        self.signin1.signin_user(L[0],L[1])
        # self.base.driver.implicitly_wait(10)
        time.sleep(5)

    def test_verifyContactsPageLabel(self):
        self.home1.click_contacts()
        time.sleep(5)
        # self.base.driver.implicitly_wait(10)

        x=self.contact.validateContactsPageLabel()
        # print(x)
        self.assertEqual(x,"Contacts","You are not in Contacts page")

    def test_createnewcontact(self):
        self.contact.createnewcontact()
        name=self.base.driver.find_element_by_xpath('(//div/text())[3]').text
        self.assertEqual(name,'bipul talukdar',"New user not created")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.base.driver.quit()


