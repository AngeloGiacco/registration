from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from assets.credentials import *
from base64 import b64decode as d
# Using Chrome to access web
driver = webdriver.Chrome(
    "/Users/angelogiacco/Documents/GitHub/registration/chromedriver") #change this to the path of your chromedriver, make sure chromedriver is the same version as your google chrome
# Open the website
driver.get('https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=e9e046e8-a98e-454a-b4db-621c8dc56861&&client-request-id=7607c35f-75b0-4d6b-80bc-ade6a25a57f2&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=143b8019-04e9-48a9-b39e-a9246dc33280&domain_hint=')
driver.maximize_window()
id_box = driver.find_element_by_name('loginfmt')
time.sleep(3)
id_box.send_keys(d(email))
# Find next button
next_button = driver.find_element_by_id('idSIButton9')
# Click next
next_button.click()

"""
only include this next bit of code if you get a personal or work account page after clicking next
"""
time.sleep(4)
div = driver.find_element_by_xpath(
    '/html/body/div/form[1]/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div')  # choose work account
div.click()

"""
remove part above if you don't get the personal or work account page
"""
time.sleep(4)
inp = driver.find_element_by_xpath(
    '/html/body/div/form[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div')
ActionChains(driver).move_to_element(inp).send_keys(
    d(password)).perform()  # enter password
time.sleep(4)
# Find next button
sign_in = driver.find_element_by_id('idSIButton9')
# Click next
sign_in.click()
time.sleep(4)
no = driver.find_element_by_xpath(
    '/html/body/div/form/div/div/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/input')
ActionChains(driver).move_to_element(no).click(no).perform()
time.sleep(10)
teams = driver.find_element_by_xpath(
    "/html/body/div[2]/div[2]/div/app-bar/nav/ul/li[5]")
ActionChains(driver).move_to_element(teams).click(teams).perform()
time.sleep(4)

"""
This next bit of code will click on the first team tile
"""

tile = driver.find_element_by_xpath(
    "/html/body/div/div[2]/div[2]/div/teams-grid/div/div[2]/div/div/div/div/div[2]/div[2]/div/ng-include/div")
ActionChains(driver).move_to_element(tile).click(tile).perform()

"""
Ensure that your house's team tile is the one in the top left when you click on teams in the left nav bar
You can put it in the top left by dragging and dropping
"""

time.sleep(4)
reg_channel = driver.find_element_by_xpath(
    "/html/body/div/div[2]/div/div/left-rail/div/div/school-app-left-rail/single-team-channel-list/div/div/div/div[3]/ul/li[2]")
ActionChains(driver).move_to_element(reg_channel).click(reg_channel).perform()
time.sleep(4)
reg_page = driver.find_element_by_xpath(
    "/html/body/div/div[2]/div[2]/div/middle-messages-stripe/div/messages-header/div/div/ng-include/div/div/ng-include[1]/div/ul/li[4]")
ActionChains(driver).move_to_element(reg_page).click(reg_page).perform()
time.sleep(4)
date = datetime.datetime.now().strftime("%d-%m-%Y") #this will get today's date
date_inp = driver.find_element_by_xpath(
    "/html/body/div[2]/div[2]/div[2]/div/middle-messages-stripe/div/messages-header/div[2]/div/base-tab/div/div/extension-tab/div/embedded-page-container/div/iframe/html/body/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div/input")
date_inp.send_keys(date)
