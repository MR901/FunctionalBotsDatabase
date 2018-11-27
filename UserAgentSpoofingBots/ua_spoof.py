from selenium import webdriver
import execjs 
from selenium.webdriver.common.keys import Keys
import time
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.ERROR)
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "whatever you want")
profile.set_preference("general.hardwareconcurrency.override", "whatever you want")
#profile.set_preference("general.MozAppearance.override", "whatever you want")
browser = webdriver.Firefox(profile)
browser.get("http://ssjswebsite.ml/test_browser.html")
#browser.execute_script("navigator.__defineGetter__('userAgent', function(){return 'jo bhi dalna hai ' });")
browser.execute_script("console.log(navigator.userAgent)")
browser.execute_script("console.log(navigator.hardwareConcurrency)")
browser.execute_script("console.log(navigator.plugins)")
