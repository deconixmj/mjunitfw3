import unittest
from selenium import webdriver
from Pages.BasePage import Basepage
from Pages.HomePage import Homepage
from Pages.SigninPage import SignIn
# from Pages.signupPage import Signup
from ddt import ddt,data,idata,unpack
from Testdata.readdata import getdata_signin


@ddt
class UserLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        url = "https://freecrm.com/"
        cls.base = Basepage(url)
        # for cap in desired_caps:
        #     cls.driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=cap)
        cls.base.driver.get(url)
        cls.home = Homepage(cls.base.driver)
        # home.click_signin()
        # cls.base.driver.implicitly_wait(30)
        cls.signin1=SignIn(cls.base.driver)
        cls.signin1.click_signin()


    def setUp(self):
        pass
        #


    # Here we are not unpacking as we are just getting the simple list from function and passing it as argument.
    @data(getdata_signin())
    # @unpack
    def test_login(self,L):
        # L=getdata_signin() this is another way to get the data.

        username=L[0]
        password=L[1]
        self.signin1.signin_user(username,password)

        # self.driver.impl
        # self.signin.driver.implicitly_wait(30)

    def test_verifylogin(self):
        t=self.signin1.login_verify()
        self.assertEqual(t,'Mj P','user is not logged in OR wrong user login')

    def test_verifyHomepagetitle(self):
        t=self.signin1.validateHomePageTitle()
        self.assertEqual(t,'Cogmento CRM','Home page title not correct')

    def test_verifycrmlogo(self):
        pass


    def tearDown(self):
        pass
        # self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.base.driver.close()





