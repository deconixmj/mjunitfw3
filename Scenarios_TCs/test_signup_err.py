import unittest
# from datetime import
from selenium import webdriver
from Pages.BasePage import Basepage
from Pages.HomePage import Homepage
from Pages.signupPage import Signup
from ddt import ddt,data,unpack
from Testdata.readdata import getdata

### import your pages and datafiles , ddt, read

# This is one integration test in which unit tests will be there.

@ddt
class newuser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        url="https://freecrm.com/"
        base=Basepage(url)
        home=Homepage(base.driver)
        home.click_sign_up()
        # sleep(5)
        cls.signup1=Signup(base.driver)


        # w_signup=base.driver.window_handles[1]
        # base.driver.switch_to_window(w_signup)


    def setUp(self):
        # self.signup1=Signup(self.driver)
        pass
        #self.signup1 = Signup(base)


    #correct values and submit
    @data(*getdata())
    # @unpack
    def test_1(self,value):
        # L=getdata()
        email=value[0]
        phone=value[1]
        self.signup1.register_user(email,phone)

        # self.signup1.register_user(email,phone)


    # validate err messages when submitted without values.
    # def test_2(self):
    #     # Signup.register_user_without_signup_err()
    #     L=[]
    #     L.append(self.signup1.register_user_without_signup_err())
    #     # print(L[0])
    #     # print(L[0][0])
    #     assert L[0][0] =="[[Email is required]]"
    #     assert L[0][1] =="[[Phone is required]]"
    #     assert L[0][2] =="[[Please accept the terms to continue]]"
    #     assert L[0][3] =="[[Please complete the Captcha]]"
    #     print("Test passed")



    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # pass

        quit()




