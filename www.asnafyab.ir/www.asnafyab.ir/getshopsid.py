
import bs4
import requests
import redis

link1="http://www.asnafyab.ir/Job/List/"

r= redis.StrictRedis(host='localhost',port=6379,db=0)

for j in range(1,330):
    print "main cat = ", j
    for l in range(1,100):
                end=1
                print "page =" , l



                try:
                  num="%d"%j
                  pagenum="?page=%d"%l
                  urli=link1+num+pagenum
                  page=requests.get(urli)
                  soup = bs4.BeautifulSoup(page.content,"lxml")

                  for a in soup.findAll('a', href=True):
                              outputurl = a['href']
                              if outputurl.startswith(("/0","/1","/2","/3","/4","/5","/6","/7","/8","/9"))  :
                                  if len(outputurl)<14 :
                                          end=0
                                          print outputurl
                                          r.incr(outputurl)





                except ValueError:
                     print("Oops!could'nt get the page!!!")
     
          
                if end == 1 :
                      print "end of page!!!"
                      break

