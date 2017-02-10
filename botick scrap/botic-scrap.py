import bs4
import requests
import redis

link1="http://www.botick.com/category/9/%D9%83%D9%8A%D9%81-%D9%88-%D9%83%D9%81%D8%B4/undefined/page/1/price/0/"
link2="/price/0/color_id/-1/zone/-1/buy_method/0"
    
r= redis.StrictRedis(host='localhost',port=6379,db=2)

for j in range(2,280):
      num="%d"%j
      urli=link1+num+link2
      page=requests.get(urli)
      soup = bs4.BeautifulSoup(page.content,"lxml")
      for a in soup.findAll("div", { "class" : "shop-item-category" }):
              outputurl = a.find('a')['href']
              print j
              print outputurl
              r.incr(outputurl) 