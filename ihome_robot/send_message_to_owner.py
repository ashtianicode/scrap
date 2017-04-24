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
amessage="hi i want to buy the house"
baseurl = "https://www.ihome.ir/%D8%B1%D9%87%D9%86-%D8%A7%D8%AC%D8%A7%D8%B1%D9%87/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AA%D9%87%D8%B1%D8%A7%D9%86/%D8%B3%D8%B9%D8%A7%D8%AF%D8%AA-%D8%A2%D8%A8%D8%A7%D8%AF/%D8%B9%D9%84%D8%A7%D9%85%D9%87-%D8%B7%D8%A8%D8%A7%D8%B7%D8%A8%D8%A7%DB%8C%DB%8C/%D8%A7%D8%AC%D8%A7%D8%B1%D9%87-%D9%88%D8%A7%D8%AD%D8%AF-116-%D9%85%D8%AA%D8%B1%DB%8C-%D8%B3%D8%B9%D8%A7%D8%AF%D8%AA-%D8%A2%D8%A8%D8%A7%D8%AF-%D8%B9%D9%84%D8%A7%D9%85%D9%87-%D8%B7%D8%A8%D8%A7%D8%B7%D8%A8%D8%A7%DB%8C%DB%8C-%D8%B5%D8%B1%D8%A7%D9%81%D9%87%D8%A7-%D8%B4%D9%85%D8%A7%D9%84%DB%8C-{}.html"
#get loggin connection
for i in range(842000,842021):
                browser = webdriver.Chrome('/home/taha/Documents/playground/selenium/chromedriver')
                browser.get(baseurl.format(i)) 
                username = browser.find_element_by_id("sender_name")
                email = browser.find_element_by_id("sender_email")
                phone = browser.find_element_by_id("sender_phone")
                message = browser.find_element_by_id("sender_message")
#               typeuser = browser.find_element_by_id("user_type")
#                typeuser = browser.find_elements_by_xpath('//*[@id="agent_aside"]/div[2]/ul/li[1]')

                
                username.send_keys(ausername)
                email.send_keys(aemail)
                phone.send_keys(aphone)
                message.send_keys(amessage)
                browser.find_element_by_class_name('chkbox_label').click()
                time.sleep(5)
                send = browser.find_element_by_id("btn_send_email")
                send.click();

