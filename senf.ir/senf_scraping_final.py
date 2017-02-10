#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import requests
import bs4
from selenium import webdriver
import shutil
import sys
reload(sys)
sys.setdefaultencoding('utf8')



link1="http://senf.ir/Company/"
link2="/%D9%85%D8%AD%D8%B5%D9%88%D9%84%D8%A7%D8%AA-%D8%AE%D9%88%D8%A7%D8%A8-%D8%AF%D9%84%D9%85%DB%8C%D8%B1%D9%87-%D9%88-%D8%AF%D9%84%D8%A7%D8%B1%D8%A7%D9%85"

chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs",prefs)



#get loggin connection
print 'trying to login :  '
browser = webdriver.Chrome('/home/taha/Documents/playground/selenium/chromedriver',chrome_options=chromeOptions)
browser.get("http://senf.ir/") 
browser.find_element_by_class_name("sideicons2").click()
username = browser.find_element_by_id("Login1_txtUserName")
password = browser.find_element_by_id("Login1_txtPassword")
username.send_keys("09360110158")
password.send_keys("09360110158212")
browser.find_element_by_id("Login1_btnEnter").click()
cookies = browser.get_cookies()
s = requests.Session()
for cookie in cookies:
    s.cookies.set(cookie['name'], cookie['value'])
print 'logged in and ready to scrap ! \n\n'

#get data 
print 'trying to open csv :  '
out = open('100k_test_output_2.csv', 'w')
writer = csv.writer(out, delimiter=",")
print 'openned the csv ! \n\n'
for num in range (140000,2100000):
                     
           ostan=shahr=gorooh=zirgorooh=address=modir=tele_localurl_short=phone_localurl_short=email_localurl_short=website=tozihat=bazdid=0
           tele=phone=email=phone_imgurl=tele_imgurl=email_imgurl=phone_wipedimgurl=tele_wipedimgurl=email_wipedimgurl=tele_finalurl=phone_finalurl=email_finalurl=r1=r2=r3=0
           phone_localurl=tele_localurl=email_localurl=0
           
           try:                  
                print 'in try loop %d: \n\n'%num                
                urli=link1+str(num)+link2
                page=s.get(urli)
                soup = bs4.BeautifulSoup(page.content,"lxml")
               
           except:
               print 'couldnt get the page! \n\n'
               
           
           try:
                ostan = soup.find('span', { 'id' : 'ContentPlaceHolder2_rpParent_lblheaderCheild_0' }).string
           except:
               print ''
           try:     
                shahr = soup.find('span', { 'id' : 'ContentPlaceHolder2_rpParent_lblheaderCheild_1' }).text
           except:
               print ''                
           try:     
                gorooh = soup.find('span', { 'id' : 'ContentPlaceHolder2_rpParent_lblheaderCheild_2' }).string
           except:
               print ''
           try:    
                zirgorooh = soup.find('span', { 'id' : 'ContentPlaceHolder2_rpParent_lblheaderCheild_3' }).string
           except:
               print ''
           try:     
                address = soup.find('span', { 'id' : 'ContentPlaceHolder2_txtAddress' }).string
           except:
               print ''
           try:                
                modir = soup.find('span', { 'id' : 'ContentPlaceHolder2_LblManager' }).string
           except:
               print ''                
           try:               
               tele = soup.find('img', { 'id' : 'ContentPlaceHolder2_ImgTell' })
           except:
               print ''           
           
           try:
                phone = soup.find('img', { 'id' : 'ContentPlaceHolder2_ImgMobil' })
           except:
               print ''
           try:    
                email = soup.find('img', { 'id' : 'ContentPlaceHolder2_ImgEmail' })
           except:
               print ''
           try:     
                website = soup.find('a', { 'id' : 'ContentPlaceHolder2_hfWebsait' }).string
           except:
               print ''
           try:    
                tozihat = soup.find('span', { 'id' : 'ContentPlaceHolder2_lblDesc' }).string
           except:
               print ''
           try:     
                bazdid = soup.find('span', { 'id' : 'ContentPlaceHolder2_lblVisit' }).string
           except:
               print ''
               
           try:    
                phone_imgurl=  phone['src']
                phone_wipedimgurl=phone_imgurl[6:]
                phone_finalurl='http://senf.ir/'+phone_wipedimgurl
                r1 = requests.get(phone_finalurl, stream=True)
                if phone_imgurl !="" and r1.status_code == 200:
                    phone_localurl='/home/taha/Documents/playground/selenium/phone_img/phone'+str(num)+'.png'
                    phone_localurl_short='phone'+str(num)+'.png'               
                    with open(phone_localurl, 'wb') as f:
                        r1.raw.decode_content = True
                        shutil.copyfileobj(r1.raw, f)   
               
           except:
               print 'no phone!'               
                                 

           try:
                tele_imgurl=  tele['src']
                tele_wipedimgurl=tele_imgurl[6:]
                tele_finalurl='http://senf.ir/'+tele_wipedimgurl
                r2 = requests.get(tele_finalurl, stream=True)
                if tele_imgurl !="" and r2.status_code == 200:
                    tele_localurl='/home/taha/Documents/playground/selenium/tele_img/tele'+str(num)+'.png'
                    tele_localurl_short='tele'+str(num)+'.png'               
                    with open(tele_localurl, 'wb') as f:
                        r2.raw.decode_content = True
                        shutil.copyfileobj(r2.raw, f)   
               
           except:
               print 'no tele !'


           try:
                email_imgurl=  email['src']
                email_wipedimgurl=email_imgurl[6:]
                email_finalurl='http://senf.ir/'+email_wipedimgurl
                r3 = requests.get(email_finalurl, stream=True)
                if email_imgurl !="" and r3.status_code == 200:
                    email_localurl='/home/taha/Documents/playground/selenium/email_img/email'+str(num)+'.png'
                    email_localurl_short='email'+str(num)+'.png'               
                    with open(email_localurl, 'wb') as f:
                        r3.raw.decode_content = True
                        shutil.copyfileobj(r3.raw, f)   
               
           
           
           except:
               print "no email ! "
           new_row =[num,ostan,shahr,gorooh,zirgorooh,address,modir,tele_localurl_short,phone_localurl_short,email_localurl_short,website,tozihat,bazdid]
          
           writer.writerow(new_row)

out.close()
