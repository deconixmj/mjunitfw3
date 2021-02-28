from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Testdata.readdata import getdata_signin
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'D:\webdrivers\geckodriver.exe')

L=getdata_signin()

# fireFoxOptions = webdriver.FirefoxOptions()
# fireFoxOptions.set_headless()
# brower = webdriver.Firefox(firefox_options=fireFoxOptions)

url="https://freecrm.com/"
# driver=webdriver.Firefox(executable_path=r'D:\webdrivers\geckodriver.exe')
driver.get(url)

driver.find_element_by_xpath("//span[contains(text(),'Log In')]").click()

driver.implicitly_wait(20)
driver.find_element_by_name('email').send_keys(L[0])
driver.find_element_by_name('password').send_keys(L[1])

driver.find_element_by_xpath('(//div[contains(text(),"Login")])[1]').click()
time.sleep(5)

action = ActionChains(driver)
x=driver.find_element_by_xpath('//i[@class="users icon"]')
# contactsicon = self.waitForElementVisibility(x)
action.move_to_element(x).perform()
x.click()
time.sleep(5)

driver.find_element_by_xpath('//button[text()="New"]').click()
time.sleep(3)

driver.find_element_by_name('first_name').send_keys('jalela1')
driver.find_element_by_name('last_name').send_keys('sambar1')
driver.find_element_by_xpath('//input[@class="search"]').send_keys("tanisqe")
time.sleep(3)

# suggestions=Select(driver.find_element_by_xpath('//i[@class="search icon"]').click())
# print(suggestions)
# s = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(By.XPATH,"//input[@class='search']"))
s=driver.find_elements_by_xpath('//div[@class="visible menu transition"]/div/span')
if len(s)==1:
    s[0].click()
else:
    for x in s:
        if x=="kpit":
            x.click()
     # print(x.text)

driver.find_element_by_xpath('//button[text()="Save"]').click()
time.sleep(4)

s1=driver.find_element_by_xpath('(//div/text())[3]').text

assert s1=='jalela1 sambar1', "new contact not created"

print("new contact created")

# s=Select(suggestions)
# options=s.options
# print(options)
# if "Add" in options:
#     options.click()
# for i in options:
#     if i=="tcs":
#         i.click()

