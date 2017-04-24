import bs4
import requests
import redis

url1="https://www.ihome.ir/%D8%B1%D9%87%D9%86-%D8%A7%D8%AC%D8%A7%D8%B1%D9%87/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AA%D9%87%D8%B1%D8%A7%D9%86/%D8%B3%D8%B9%D8%A7%D8%AF%D8%AA-%D8%A2%D8%A8%D8%A7%D8%AF/5/"

r= redis.StrictRedis(host='localhost',port=6379,db=0)

for j in range(1,10):
    try:     
      num="%d"%j
      urli=url1+num+"/"
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