from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Basepage:

    driver=""
    def __init__(self,url):
        # self.driver=webdriver.Firefox(executable_path=r'D:\webdrivers\geckodriver.exe')  ## browser driver object
        self.driver=webdriver.Chrome(executable_path="D:\webdrivers\88\chromedriver_win32\chromedriver.exe")

        # headless chrome
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.maximize_window()
        self.driver.get(url)
        # oopens the page
        # BROWSERSTACK_URL = 'https://manashjyotipatha1:sUShAnpfFTThw3sRyXWq@hub-cloud.browserstack.com/wd/hub'
        #
        # for cap in desired_caps:
        #     self.driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=cap)
        #     Thread(target=self.driver, args=(cap,)).start()




