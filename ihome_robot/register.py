# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver

ausername= 'booboo'
aemail="bobo@booobo.com"
aphone="09120000000"

baseurl = "https://www.ihome.ir/%D8%AB%D8%A8%D8%AA-%D9%86%D8%A7%D9%85.html"

for i in range(842000,842011):
                browser = webdriver.Chrome('/home/taha/Documents/playground/selenium/chromedriver')
                browser.get(baseurl) 
                username = browser.find_element_by_id("name")
                email = browser.find_element_by_id("email")
                phone = browser.find_element_by_id("reg_password")
                message = browser.find_element_by_id("reg_password_again")
                mobile
                chkbox_label
#               typeuser = browser.find_element_by_id("user_type")
                typeuser = browser.find_elements_by_xpath('//*[@id="agent_aside"]/div[2]/ul/li[1]')

                
                username.send_keys(ausername)
                email.send_keys(aemail)
                phone.send_keys(aphone)
                message.send_keys(amessage)
                typeuser.click()
                browser.find_element_by_class_name('chkbox_label').click()
                time.sleep(5)
                send = browser.find_element_by_id("btn_send_email")
                send.click();
