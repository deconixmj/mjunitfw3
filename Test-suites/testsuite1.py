import unittest
import HtmlTestRunner

from Scenarios_TCs.test_UserLogin import UserLogin
from Scenarios_TCs.test_CreateNewContact import TestNewContact
from Scenarios_TCs.test_DealsPage import TestDealsPage

tc1=unittest.TestLoader().loadTestsFromTestCase(UserLogin)
tc2=unittest.TestLoader().loadTestsFromTestCase(TestNewContact)
tc3=unittest.TestLoader().loadTestsFromTestCase(TestDealsPage)

test_suite=unittest.TestSuite([tc1,tc2,tc3])

test_runner=HtmlTestRunner.HTMLTestRunner(output='D:\Py_projects\mjunitfw3_testsuite_nose\\reports')



