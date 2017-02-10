# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:04:47 2016

@author: taha
"""

import bs4
import requests
import redis

link1="http://ebazar.post.ir/cats/home/safety-accessories/"
    
r= redis.StrictRedis(host='localhost',port=6379,db=6)

for j in range(1,290):
    try:     
      num="%d"%j
      urli=link1+num
      page=requests.get(urli)
      soup = bs4.BeautifulSoup(page.content,"lxml")
      
      for a in soup.findAll("h2", { "class" : "product-name" }):
                   outputurl = a.find('a')['href']
                   print j
                   print outputurl
                   r.incr(outputurl) 
                   
    except ValueError:
         print("Oops!  That was no valid number.  Try again...")