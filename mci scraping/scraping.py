# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import bs4
import requests
import redis

r= redis.StrictRedis(host='localhost',port=6379,db=0)
page=requests.get('***********')
soup = bs4.BeautifulSoup(page.content,"lxml")
name= soup.findAll("div", { "class" : "product-page-name" })
shop= name[1].string

