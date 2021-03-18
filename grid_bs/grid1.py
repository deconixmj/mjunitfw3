import unittest
from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_caps=[{
      'os_version': 10,
      'os': 'Windows',
      'browser': 'Chrome',
      'browser_version': '80',
      'name': 'Test1', # test name
      'build': 'parallel-build-python' # Your tests will be organized within this build
      },
      {
      'os_version' : '10.0',
      'device' : 'Samsung Galaxy S20',
      'real_mobile' : 'true',
      'name': 'Test2',
      'build': 'parallel-build-python'
      },
      {
      'os_version' : '14',
      'device' : 'iPhone XS',
      'real_mobile' : 'true',
      'name': 'Test3',
      'build': 'parallel-build-python'
      },
      {
      'os_version': 10,
      'os': 'Windows',
      'browser': 'Firefox',
      'browser_version': 'latest',
      'name': 'Test4',
      'build': 'parallel-build-python'
      },
      {
      'os_version' : 'Catalina',
      'os': 'OS X',
      'browser': 'Safari',
      'browser_version': 'latest',
      'name': 'Test5',
      'build': 'parallel-build-python'
}]

BROWSERSTACK_URL = 'https://manashjyotipatha1:sUShAnpfFTThw3sRyXWq@hub-cloud.browserstack.com/wd/hub'


def run_session(desired_cap):
    //testcases



#The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session parallelly

for cap in desired_caps:
    Thread(target=run_session, args=(cap,)).start()
