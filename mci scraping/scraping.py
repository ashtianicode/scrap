# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import bs4
import requests
import redis

r= redis.StrictRedis(host='localhost',port=6379,db=0)
page=requests.get('http://www.botick.com/category/6/%D9%84%D8%A8%D8%A7%D8%B3-%D9%85%D8%B1%D8%AF%D8%A7%D9%86%D9%87')
soup = bs4.BeautifulSoup(page.content,"lxml")
name= soup.findAll("div", { "class" : "product-page-name" })
shop= name[1].string

