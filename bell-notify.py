import os
import time
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("https://www.lankabell.com/lte/")

inputUser = driver.find_element_by_id("logName")
inputUser.send_keys('<username here>')
inputPass = driver.find_element_by_id("password")
inputPass.send_keys('<password here>')
inputPass.send_keys(Keys.ENTER)
time.sleep(5)
driver.get("https://www.lankabell.com/lte/usage.jsp")
time.sleep(2)
try:
    fieldPK = driver.find_element_by_id("PkRemain")
    PKRem = fieldPK.get_attribute("value")
    fieldOPK = driver.find_element_by_id("OPkRemain")
    OPKRem = fieldOPK.get_attribute("value")
    PKRem = round(float(PKRem)/(1024*1024), 2)
    OPKRem = round(float(OPKRem)/(1024*1024), 2)
    os.system(
        "notify-send -u low ' Peak: {}GB\n Off-Peak: {}GB'".format(PKRem, OPKRem))
except:
    os.system("notify-send 'Something went wrong, Please try again!'")

time.sleep(3)
print("exiting")
driver.quit()
