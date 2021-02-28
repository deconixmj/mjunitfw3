from selenium import webdriver

url="https://freecrm.com/"
driver=webdriver.Firefox(executable_path=r'D:\webdrivers\geckodriver.exe')
driver.get(url)

#driver.find_elements_by_link_text('SIGN UP').click()
driver.find_element_by_xpath('(//a[@href="https://register.freecrm.com/register/"])[2]').click()
#window1=driver.window_handles[1]
#driver.switch_to.window(window1)

driver.find_element_by_name("action").click()

## validate error messages

error_email=driver.find_element_by_xpath('//div[@class="ui negative message"]/ul/li[1]').text
print(error_email)

assert error_email=="[[Email is required]]"
print("test pass")