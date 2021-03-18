import unittest
import HtmlTestRunner
import time
from multiprocessing import Pool

# class runner(HtmlTestRunner):
#     def run(ts):
#         p=Pool(processes=3)
#         p.map()

def run():
    p=Pool(processes=3)
    p.map(runner,[tc1,tc2,tc3])

from Scenarios_TCs.test_UserLogin import UserLogin
from Scenarios_TCs.test_CreateNewContact import TestNewContact
from Scenarios_TCs.test_DealsPage import TestDealsPage

tc1=unittest.TestLoader().loadTestsFromTestCase(UserLogin)
tc2=unittest.TestLoader().loadTestsFromTestCase(TestNewContact)
tc3=unittest.TestLoader().loadTestsFromTestCase(TestDealsPage)

# test_suite=unittest.TestSuite([tc2])

test_runner=HtmlTestRunner.HTMLTestRunner(output='D:\Py_projects\mjunitfw3_testsuite_nose\\reports')

def runner(tc):
    test_runner.run(tc)

if __name__ == '__main__':
    exit(run())


