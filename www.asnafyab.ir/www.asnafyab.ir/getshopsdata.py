#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import requests
import bs4
import csv
#import sys
#import traceback
#reload(sys)
#sys.setdefaultencoding('utf8')



r= redis.StrictRedis(host='localhost',port=6379, db=2)

subjects=[]



urls = r.keys()
out = open('datas1to17.csv', 'w')
writer = csv.writer(out, delimiter=",")
page=requests.get("http://www.asnafyab.ir/33981536")
soup = bs4.BeautifulSoup(page.content,"lxml")
  
for a in soup.findAll("div", { "class" : "JobDetail" }) : 
           spans = soup.findAll("span")
           
           for s in spans :
               subjects.append(s)
                           
           
print "this is subjects:"
print subjects[1]
print subjects[3]
print subjects[5]
print subjects[7]
print subjects[9]
print subjects[11]
print subjects[13]
print subjects[14]



for i in range(1,17) :
                 print i

                
                 try:

                    page=requests.get("http://www.asnafyab.ir/" + urls[i])
                    soup = bs4.BeautifulSoup(page.content,"lxml")
                    
                    sharh=modir=tamas=hamrah=mantaghe=address=website=email=""  
                    for a in soup.findAll("div", { "class" : "JobDetail" }) : 
                    
                              
                              
                               spans = soup.findAll("span")
                               
                               for s in spans:
                                   
                                   if s == subjects[1]:
                                       index = spans.index(s)
                                       sharh= spans[index+1].text.encode("utf-8")
                                        
                                   if s == subjects[3]:
                                       index = spans.index(s)
                                       modir= spans[index+1].text.encode("utf-8")
    
    
                                   if s == subjects[5]:
                                       index = spans.index(s)
                                       tamas = spans[index+1].text.encode("utf-8")
    
                                   if s == subjects[7]:
                                       index = spans.index(s)
                                       hamrah= spans[index+1].text.encode("utf-8")
    
                                   if s == subjects[9]:
                                       index = spans.index(s)
                                       mantaghe= spans[index+1].text.encode("utf-8")
    
                                   if s == subjects[11]:
                                       index = spans.index(s)
                                       address= spans[index+1].text.encode("utf-8")
    
    
                                   if s == subjects[13]:
                                       index = spans.index(s)
                                       website= "دارد"
    
    
                                   if s == subjects[14]:
                                       index = spans.index(s)
                                       email= "دارد"
    
    
    
             
    
    
    
                    new_row=[sharh,modir,tamas,hamrah,mantaghe,address,website,email]
                    writer.writerow(new_row)

                 except:
                     print "oh no"

out.close()
    
    
   