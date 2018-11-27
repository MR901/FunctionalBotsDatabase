
def LoginThroughFacebook(UsrAndPass):
    print('Trying To Login Using Facebook')
#     LoginWithFacebookButton = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/button[1]"
    LoginWithFacebookButton = '/html/body/div[2]/div/div/div[2]/div/div[3]/div[1]/button'
    
    try:
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((By.XPATH, LoginWithFacebookButton))) #'//*[@id="hplogo"]'
        time.sleep(randint(2, 3))
    except:
        print("Timeout Occured in Login")
    
    
    try:
        elem = driver.find_element_by_xpath(LoginWithFacebookButton)
        window_before = driver.window_handles[0]
        elem.click()

        window_after = driver.window_handles[1]
        time.sleep(15)
        driver.switch_to_window(window_after)
        
        if (driver.title == 'Facebook'):
            elem = driver.find_element_by_id("email")
            elem.send_keys(UsrAndPass[0])
            elem = driver.find_element_by_id("pass")
            elem.send_keys(UsrAndPass[1])
            elem.send_keys(Keys.RETURN)
            elem.click()
            ## Login complete

            driver.switch_to_window(window_before)
            print('Login by Facebook Completed')
        else:
            print('Failed To login')
            
    except:
        print("Some Error Occured In Login Through Facebook")
        time.sleep(1)
        sys.exit("Some Error Occured In Login Through Facebook")
        # pass
    
def GetToSwipePage():
    
#     try:
#         
#         while !(driver.find_element_by_xpath(ScreenTextXPath_This).is_displayed() and driver.find_element_by_xpath(ScreenTextXPath_This).text == 'Welcome to Tinder'):
#             time.sleep(1)
#     except:
#         pass
    
    try:
        ScreenTextXPath_This = '/html/body/div[1]/div/span/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/span'
        wait = WebDriverWait(driver, 120)
        wait.until(EC.presence_of_element_located((By.XPATH, ScreenTextXPath_This))) #'//*[@id="hplogo"]'
        time.sleep(randint(2, 3))
    except:
        print("Timeout Occured")
    
    def TryUntilButtonAppearAndThenClick(NextbuttonXPath, ScreenTextXPath_This, TextLike):
        try:
            NxtElem = driver.find_element_by_xpath(NextbuttonXPath)
            ScrTxtElem = driver.find_element_by_xpath(ScreenTextXPath_This)
            while NxtElem.is_displayed() and ScrTxtElem.text == TextLike:
                NxtElem = driver.find_element_by_xpath(NextbuttonXPath)
                ScrTxtElem = driver.find_element_by_xpath(ScreenTextXPath_This)
                time.sleep(randint(2, 3))
                NxtElem.click()
        except:
            print('Screen Changed from {}'.format(TextLike))
    
    
    NextbuttonXPath = "/html[1]/body[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]/span[1]/span[1]"
    ScreenTextXPath_This = '/html/body/div[1]/div/span/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/span'
    TryUntilButtonAppearAndThenClick(NextbuttonXPath, ScreenTextXPath_This, 'Welcome to Tinder')

    NextbuttonXPath = "/html/body/div[1]/div/span/div/div[2]/div/div/main/div/div[3]/button"
    ScreenTextXPath_This = '/html/body/div[1]/div/span/div/div[2]/div/div/main/div/div[2]/div[1]/span'
    TryUntilButtonAppearAndThenClick(NextbuttonXPath, ScreenTextXPath_This, 'Enhanced Messaging')

    NextbuttonXPath = "/html[1]/body[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]/span[1]/span[1]"
    ScreenTextXPath_This = '/html/body/div[1]/div/span/div/div[2]/div/div/div[1]/div/div[2]/div[1]/span'
    TryUntilButtonAppearAndThenClick(NextbuttonXPath, ScreenTextXPath_This, 'Share Your Location')

    NextbuttonXPath = "/html[1]/body[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]/span[1]/span[1]"
    ScreenTextXPath_This = '/html/body/div[1]/div/span/div/div[2]/div/div/div[1]/div/div[2]/div[1]/span'
    TryUntilButtonAppearAndThenClick(NextbuttonXPath, ScreenTextXPath_This, 'Enable Notifications')
    
    print('Arrived on Swiping Page')
    
    
    
    
########################################################## ## # Main Program # ## #####
# %tb to check error
## impot libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time, os, sys
from random import randint
import pandas as pd
#!pip install PyExecJS
import execjs.runtime_names

# UsrAndPass = ("asdfgh@gmail.com", "password")
UsrAndPass = ("LoginID Facebook", "Pass")


## Initiating a new profile
profile = webdriver.FirefoxProfile()
# https://stackoverflow.com/questions/38316910/python-selenium-what-are-possible-keys-in-firefox-webdriver-profile-preference?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
#profile.set_preference('browser.download.folderList', 2)
#profile.set_preference('browser.download.manager.showWhenStarting', False)
#profile.set_preference('browser.download.dir', os.getcwd())
#profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv/xls')
profile.set_preference("geo.enabled", True)
profile.set_preference("geo.provider.use_corelocation", True)
profile.set_preference("geo.prompt.testing", False)
profile.set_preference("geo.prompt.testing.allow", False)


print("Program Start")
driver = webdriver.Firefox(profile)
#driver = webdriver.Firefox()

driver.get("https://tinder.com")

time.sleep(20)
print('Trying to login')
LoginThroughFacebook(UsrAndPass)
time.sleep(randint(2, 3))
GetToSwipePage()
