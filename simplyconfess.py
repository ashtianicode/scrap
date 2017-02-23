# -*- coding: utf-8 -*-




import requests
import bs4
import sys
from random import randint
reload(sys)
sys.setdefaultencoding('utf-8')
categories =[['o','other'],['d','a-dream'],['f','a-fantasy'],['fi','a-first-experience'],['g','a-guilt'],['l','a-lie'],['p','a-pain'],['q','a-question'],['r','a-random-feeling'],['t','a-truth'],['w','a-wild-experience']]
url = "http://localhost:8080/web/post/submit/"





def gettexts(hyperlinks):
    paragraphes=[]
    for t in hyperlinks:
        page = requests.get(t)
        soup = bs4.BeautifulSoup(page.content,"lxml")
        text = soup.find_all("div",{"class":"entry-content"})        
        for p in text:
            paras =p.find_all("p")
            for para in paras :
                paragraph = para.text
                paragraphes.append(paragraph)
                print len(paragraphes)
    return  paragraphes            
        

for rand in range(1,1000) :
        r = randint(0,10)
        categoryurl= categories[r][1]
        confessmode= categories[r][0]
        print categoryurl,confessmode
        mainurl ="http://www.simplyconfess.com/category/"
        pages=[]
        firstpage = requests.get(mainurl+categoryurl)
        soup = bs4.BeautifulSoup(firstpage.content,"lxml")
        numbers = soup.find_all("ul",{"class":"pagination"})
        for n in numbers :
            listitem = n.find_all("a")
            for l in listitem:
                numberofpages=l.text
                pages.append(numberofpages)
                
             
        
        lastpage = pages[-2]
        hyperlinks=[]
        finalurl= mainurl+ categoryurl + "/page/" +str(randint(0,int(lastpage)))
        page= requests.get(finalurl)
        soup =bs4.BeautifulSoup(page.content,"lxml")
        links =soup.find_all("div",{"class":"entry-content hvr-grow"})
        i= 0
        link = links[0]  
        hyperlinks.append( link['data-post-url'])
        print len(hyperlinks)    
        for pp in gettexts(hyperlinks)   :
                
                    requests.post(url, data = {'text':pp.encode('utf-8'),'mode':confessmode})


                 
                 

                 
                 
                 
                 
