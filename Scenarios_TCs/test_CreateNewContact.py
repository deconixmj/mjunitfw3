'''
For Contact page , all testcases can be within this same test class.
Algnwith pom , you need to design the test cases too.


'''

import unittest
import time
from selenium import webdriver
from Pages.BasePage import Basepage
from Pages.HomePage import Homepage
from Pages.SigninPage import SignIn
from Pages.ContactsPage import ContactsPage
# from Pages.signupPage import Signup
from ddt import ddt,data,idata,unpack
from Testdata.readdata import getdata_signin,getcontacts_data

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
        L = getdata_signin()
        cls.signin1.signin_user(L[0],L[1])

    def setUp(self):
        # self.contactshome=Homepage(self.base.driver)

        # self.base.driver.implicitly_wait(10)

        icon = "users"
        self.home.click_icons(icon)
        time.sleep(15)

    def test_a_verifyContactsPageLabel(self):

        x=self.contact.validateContactsPageLabel()
        # print(x)
        self.assertEqual(x,"Contacts","You are not in Contacts page")

    #pass values using ddt.data decorator
    @data(*getcontacts_data())
    @unpack
    def test_b_createnewcontact(self,fname,lname,company):
        name=self.contact.createnewcontact(fname,lname,company)
        contact_name=fname+ " " +lname
        # xpath1='//div[text()="{}"]'.format(contact_name)
        # name=self.base.driver.find_element_by_xpath(xpath1).text
        self.assertEqual(name,contact_name,"New user not created")

    def test_editcontact(self):
        pass


    def test_deletecontact(self):
        pass


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.base.driver.quit()


