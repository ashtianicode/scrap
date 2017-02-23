# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import bs4
categories =['other','a-dream','a-fantasy']





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
        

for cat in categories :
        categoryurl= cat
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
        for i in range(1,int(lastpage)):
            
            
                hyperlinks=[]
                finalurl= mainurl+ categoryurl + "/page/" +str(i)
                page= requests.get(finalurl)
                soup =bs4.BeautifulSoup(page.content,"lxml")
                links =soup.find_all("div",{"class":"entry-content hvr-grow"})
                i= 0
                for link in links  :
                    i= i+1
                    if i==21 :
                        break
                    hyperlinks.append( link['data-post-url'])
                print len(hyperlinks)    
                for pp in gettexts(hyperlinks)   :
                    print pp

                 
                 

                 
                 
                 
                 
