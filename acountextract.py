# -*- coding: utf-8 -*-
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver
usernum= '*'
passw='*'
#get loggin connection

browser = webdriver.Chrome('/home/taha/Documents/playground/selenium/chromedriver')
browser.get("http://poloto.ir/portal") 
username = browser.find_element_by_id("contentplaceholder1_login_login1_Username")
password = browser.find_element_by_id("contentplaceholder1_login_login1_Password")
username.send_keys(usernum)
password.send_keys(passw)
browser.find_element_by_class_name('contentplaceholder1_login_login1micro_login_button').click()
for page in range(3,8):
        x=page*50
        y=x-50
        for i in range(1,48):  
            time.sleep(1)
            browser.execute_script("Menu_XMenusseturl('/portal/?clients');")
            browser.execute_script("ContentPlaceHolder1_portal_Clients_Paginggotopage(%d,%d,%d,'double')"%(page,y,x))
            idjs = browser.find_elements_by_class_name('serviceitem')[i].get_attribute("ondblclick")
            browser.execute_script(idjs)
            email = browser.find_element_by_id('ContentPlaceHolder1_portal_Clients_ClientRgListbaseitem3_fINPUT').get_attribute("value")
            passemail = browser.find_element_by_id('ContentPlaceHolder1_portal_Clients_ClientRgListbaseitem4_fINPUT').get_attribute("value")
            if email[-10:] =="@gmail.com"    :
                
                 print email,'      ',passemail
            
        
