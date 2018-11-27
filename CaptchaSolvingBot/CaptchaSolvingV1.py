from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.cache.disk.enable", False)
profile.set_preference("browser.cache.memory.enable", False)
profile.set_preference("browser.cache.offline.enable", False)
profile.set_preference("network.http.use-cache", False) 
driver =webdriver.Firefox(profile)
#driver = webdriver.Firefox()

driver.get("https://patrickhlauke.github.io/recaptcha/")

driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
elem = driver.find_elements_by_class_name("recaptcha-checkbox-checkmark")
#driver.manage().deleteAllCookies()
if len(elem) > 0:
    #print "***"
    elem[0].click()
time.sleep(20)
#driver.find_element_by_xpath("//input[@id='recaptcha-token']/div//div[@id ='rc-imageselect']")

print elem
print "*****"
#elem.click()

