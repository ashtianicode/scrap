#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import requests
import bs4
import sys
import urllib
reload(sys)
sys.setdefaultencoding('utf8')



r= redis.StrictRedis(host='localhost',port=6379, db=0)


urls = r.keys()
index=0

for url in urls :
    page=requests.get("http://www.botick.com"+url)
    soup = bs4.BeautifulSoup(page.content,"lxml")
    for a in soup.findAll("img", { "itemprop" : "image" }) :
                    index=index+1
                    uuu= a['src']
                    print uuu
                    urllib.urlretrieve(uuu, "image/0000000%d.jpg"%index)

         
    
           
  
 