#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import requests
import bs4
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')



r= redis.StrictRedis(host='localhost',port=6379, db=0)


urls = r.keys()
out = open('outtest_both.csv', 'w')
writer = csv.writer(out, delimiter=",")
for url in urls :
    page=requests.get("http://www.botick.com"+url)
    soup = bs4.BeautifulSoup(page.content,"lxml")
  
    for a in soup.findAll("h1", { "itemprop" : "name" }) :
           
           name= a.text
           
         
    
    for b in soup.findAll("div", { "id" : "phone" }) :
           phonenum=b.text
           
    new_row =[name,phonenum]
    print new_row
    writer.writerow(new_row)

out.close()
    
    
   
