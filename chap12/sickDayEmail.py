#! python
# Usage: python3 cmdLineEmailer.py text_to_email

from selenium import webdriver
import sys
import pyinputplus as pyip
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import time

emailAddress = pyip.inputStr("What's your email address for your work email?\n")
password = pyip.inputPassword("What's the password for your work email?\n")
sendTo = pyip.inputStr("What's the email address you'd like to send to?\n")
subject = str(datetime.date.today()) + ': Taking a Sick Day'
message = ''' Hi,

I'm taking a sick day today, not feeling too well.

Hopefully I'll feel better tomorrow.

Thank you,

Shing.
'''

# open browser
browser = webdriver.Chrome()
browser.maximize_window()

# navigate to email site
browser.get("https://www.sfu.ca/sfumail.html")

# input the emailAddress
htmlElem = browser.find_element_by_css_selector("#page-content > section > div.main_content.parsys > div.parsys_column.cq-colctrl-lt5 > div.parsys_column.cq-colctrl-lt5-c1 > div:nth-child(1) > div > h5 > a")
htmlElem.click()

htmlElem = browser.find_element_by_css_selector("#username")
htmlElem.send_keys(emailAddress)

htmlElem = browser.find_element_by_css_selector("#password")
htmlElem.send_keys(password)

htmlElem = browser.find_element_by_css_selector("#fm1 > input.btn.btn-block.btn-submit")
htmlElem.click()
time.sleep(5)

# clicking on compose button
htmlElem = browser.find_element_by_css_selector("#primaryContainer > div:nth-child(7) > div > div._n_T > div > div._n_X > div._n_X > div > div._n_r1 > div > div > div:nth-child(1) > div > button._fce_h._fce_f.ms-fwt-r.ms-fcl-np.o365button")
htmlElem.click()

# waiting for window to pop up
time.sleep(8)

# put in recipient
htmlElem = browser.find_element_by_css_selector("#primaryContainer > div:nth-child(7) > div > div._n_T > div > div._n_X > div:nth-child(3) > div > div._n_Y > div.allowTextSelection > div > div._mcp_T2._mcp_W2 > div._mcp_U2._mcp_W2.customScrollBar.scrollContainer._mcp_Y2 > div > div._mcp_d1.ms-border-color-neutralLight > div._mcp_e1.ms-bg-color-white > div:nth-child(2) > div._mcp_f1 > div.ms-bg-color-white.customScrollBar.ms-border-color-themeTertiary > div:nth-child(2) > div:nth-child(2) > div._mcp_L1._mcp_M1._mcp_P1 > div > div > div > span > div._fp_F > form > input")
htmlElem.send_keys(sendTo)
htmlElem.send_keys(Keys.TAB)

# putting in the subject
htmlElem = browser.find_element_by_css_selector("#primaryContainer > div:nth-child(7) > div > div._n_T > div > div._n_X > div:nth-child(3) > div > div._n_Y > div.allowTextSelection > div > div._mcp_T2._mcp_W2 > div._mcp_U2._mcp_W2.customScrollBar.scrollContainer._mcp_Y2 > div > div._mcp_d1.ms-border-color-neutralLight > div._mcp_e1.ms-bg-color-white > div:nth-child(2) > div._mcp_f1 > div.ms-bg-color-white.customScrollBar.ms-border-color-themeTertiary > div:nth-child(2) > div._mcp_o1._mcp_r1._mcp_x1.ms-border-color-neutralTertiaryAlt > div._mcp_82 > input")
htmlElem.send_keys(subject)
htmlElem.send_keys(Keys.TAB)

# entering message into compose box
htmlElem = browser.find_element_by_css_selector("#primaryContainer > div:nth-child(7) > div > div._n_T > div > div._n_X > div:nth-child(3) > div > div._n_Y > div.allowTextSelection > div > div._mcp_T2._mcp_W2 > div._mcp_U2._mcp_W2.customScrollBar.scrollContainer._mcp_Y2 > div > div._mcp_d1.ms-border-color-neutralLight > div._mcp_e1.ms-bg-color-white > div:nth-child(2) > div._mcp_z1.ms-border-color-themeTertiary > div._mcp_22 > div > div._z_41.ms-bg-color-white > div:nth-child(1) > div:nth-child(3) > div > p")
htmlElem.send_keys(message)
time.sleep(2)

# sending the email
htmlElem = browser.find_element_by_css_selector("#primaryContainer > div:nth-child(7) > div > div._n_T > div > div._n_X > div:nth-child(3) > div > div._n_Y > div.allowTextSelection > div > div._mcp_T2._mcp_W2 > div._mcp_U2._mcp_W2.customScrollBar.scrollContainer._mcp_Y2 > div > div._mcp_d1.ms-border-color-neutralLight > div._mcp_e1.ms-bg-color-white > div._mcp_g1._mcp_x1.ms-bg-color-white.ms-border-color-themeTertiary > div._mcp_i1 > div._mcp_H2 > button._mcp_62.o365button.o365buttonOutlined.ms-font-m.ms-fwt-sb.ms-fcl-w.ms-bgc-tp.ms-bcl-tp.ms-bgc-td-f.ms-bcl-tdr-f")
htmlElem.click()

print("Email has been sent! Enjoy your sick day :)")