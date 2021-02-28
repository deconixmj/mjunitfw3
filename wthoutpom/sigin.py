from selenium import webdriver
from Testdata.readdata import getdata_signin

L=getdata_signin()
url="https://freecrm.com/"
driver=webdriver.Firefox(executable_path=r'D:\webdrivers\geckodriver.exe')
driver.get(url)

driver.find_element_by_xpath("//span[contains(text(),'Log In')]").click()

driver.implicitly_wait(20)
driver.find_element_by_name('email').send_keys(L[0])
driver.find_element_by_name('password').send_keys(L[1])

driver.find_element_by_xpath('(//div[contains(text(),"Login")])[1]').click()

t=driver.find_element_by_xpath('//span[contains(text(),"Mj P")]').text

assert t=='Mj P', 'wrong login'

# driver.find_element_by_xpath()
