import requests
import bs4
import redis

s = requests.session()

login =s.get("*****************")


page= s.get('********************8')


soup = bs4.BeautifulSoup(page.content,"lxml")


r= redis.StrictRedis(host='localhost',port=6379,db=5)


for a in soup.findAll("td", { "class" : "getuidbyclass" }):
              uid = a.text
              r.incr(uid)
              print uid 
