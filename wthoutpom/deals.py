from selenium import webdriver
from Testdata.readdata import getdata_signin
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time


L=getdata_signin()

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)
url="https://freecrm.com/"
driver=webdriver.Firefox(executable_path=r'D:\webdrivers\geckodriver.exe')
driver.get(url)

driver.find_element_by_xpath("//span[contains(text(),'Log In')]").click()

driver.implicitly_wait(20)
driver.find_element_by_name('email').send_keys(L[0])
driver.find_element_by_name('password').send_keys(L[1])

driver.find_element_by_xpath('(//div[contains(text(),"Login")])[1]').click()

time.sleep(10)

driver.find_element_by_xpath('//i[@class="money icon"]').click()
time.sleep(3)

driver.find_element_by_xpath('//button[text()="New"]').click()
driver.find_element_by_name('title').send_keys("My new deal mphy11")

driver.find_element_by_xpath('//button[text()="Public"]').click()

state=driver.find_element_by_xpath('//button[text()="Private"]').get_attribute('class')
st1=driver.find_element_by_xpath('//i[@class="lock icon"]').get_attribute('class')

s1=driver.find_elements_by_name("stage")
s1[0].click()
# driver.find_element_by_xpath("(//div[@name='stage'][1])[1]").click()
# xpath1=s1[2]
# driver.find_element_by_xpath(xpath1).click()

stage="Won"

for i in range(len(s1)):
    if s1[i].text==stage:
        s1[i].click()
        break





# assert st1=="lock icon", "toggle switch failed"
#
# print(state)
# print(st1)


# s=driver.find_element_by_name('stage')
# s1=Select(s)
# s1.select_by_visible_text('Prospect')
#
# st1=driver.find_element_by_name('status')
# st2=Select(st1)
# st2.select_by_visible_text('New')
