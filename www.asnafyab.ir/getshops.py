

import bs4
import requests
import redis

link1="http://www.asnafyab.ir/Job/List/"
    
r= redis.StrictRedis(host='localhost',port=6379,db=1)

for j in range(1,290):
    try:     
      num="%d"%j
      urli=link1+num
      page=requests.get(urli)
      soup = bs4.BeautifulSoup(page.content,"lxml")
      
      for a in soup.findAll('a', href=True):
                  outputurl = a['href']
                  if outputurl.startswith(("/0","/1","/2","/3","/4","/5","/6","/7","/8","/9"))  :
                      if len(outputurl)<14 :
                              print outputurl
                              r.incr(outputurl) 
                   
    except ValueError:
         print("Oops!  That was no valid number.  Try again...")