from selenium import webdriver

class Basepage:

    driver=""
    def __init__(self,url):
        # self.driver=webdriver.Firefox(executable_path=r'D:\webdrivers\geckodriver.exe')  ## browser driver object
        self.driver=webdriver.Chrome(executable_path="D:\webdrivers\88\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(url)

        # oopens the page



