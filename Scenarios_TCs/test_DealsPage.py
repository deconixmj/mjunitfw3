import unittest
import time,logging
from selenium import webdriver
from Pages.BasePage import Basepage
from Pages.HomePage import Homepage
from Pages.SigninPage import SignIn
from Pages.DealsPage import DealsPage
from ddt import ddt,data,idata,unpack
from Testdata.readdata import getdata_signin
from Testdata.readdata1 import getData1

# from Pages.ContactsPage import ContactsPage
# from Pages.signupPage import Signup

@ddt
class TestDealsPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        url = "https://freecrm.com/"
        cls.base = Basepage(url)
        cls.home = Homepage(cls.base.driver)
        cls.signin1 = SignIn(cls.base.driver)

        cls.signin1.click_signin()
        cls.deals=DealsPage(cls.base.driver)

        logging.basicConfig(filename="TitleVerification.log", format='%(asctime)s :%(levelname)s: %(message)s',filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        L = getdata_signin()
        cls.signin1.signin_user(L[0], L[1])
        # self.base.driver.implicitly_wait(10)
        time.sleep(5)

        # cls.home1 = Homepage(cls.base.driver)
        # cls.contact = ContactsPage(cls.base.driver)

    def setUp(self):
        pass

        # self.base.driver.implicitly_wait(10)


    def test_a_validateDealslabel(self):
        icon="money"
        self.home.click_icons(icon)
        time.sleep(15)

        t=self.deals.verify_dealspagelabel()
        self.assertEqual(t,"Deals","You are not in deals Page")

    @data(*getData1())
    @unpack
    def test_b_createnewdeal(self,a0,a1,a2):
        # a0=L[0]
        # a1=L[1]
        # a2=L[3]
        print(a0,a1,a2)
        st2,t=self.deals.validate_newdeal(a0,a1,a2)
        time.sleep(3)
        # self.base.driver.find_element_by_xpath('//div[text()=a0]')
        try:
            self.assertEqual(st2,'lock icon','Toggle switch did not work')
            logging.info("toggle switch pass: {}".format(st2))
        except AssertionError:
            logging.error("toggle switch failed: {}".format(st2))

        try:
            self.assertEqual(t,a0,'your deal creation page did not work')
            logging.info("deal creation passed:{}".format(t))
        except AssertionError:
            logging.error("deal creation failed: {}".format(t))


    def test_editdeal(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.base.driver.quit()

