#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import requests
import bs4
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')



r= redis.StrictRedis(host='localhost',port=6379, db=5)


urls = r.keys()
out = open('portaldataout12.csv', 'w')
writer = csv.writer(out, delimiter=",")



s = requests.session()

r =s.get("*************** ></l>")

print r.text



for url in urls :
 

               try:     
                     
                                   
                    
                    userurl="**********8"+url
                    page=s.get(userurl)
                    soup = bs4.BeautifulSoup(page.content,"lxml")
                    a=b=c=d=e=f=''
                    for a in soup.findAll("input", { "id" : "ContentPlaceHolder1_portal_Clients_ClientRgListbaseitem1_fINPUT" }) :
                                   name= a['value']
                                   print name
                         
                    
                    for b in soup.findAll("input", { "id" : "ContentPlaceHolder1_portal_Clients_ClientRgListbaseitem2_fINPUT" }) :
                                  family=b['value']
                                  print family
                    
                    for c in soup.findAll("input", { "id" : "ContentPlaceHolder1_portal_Clients_ClientRgListbaseitem3_fINPUT" }) :
                                  email=c['value']
                                  print email
                                  
                    for d in soup.findAll("input", { "id" : "ContentPlaceHolder1_portal_Clients_ClientRgListbaseitem5_fINPUT" }) :
                                  number=d['value']
                                  print number                  
                           
                   
                    
                    new_row =[name,family,email,number]
                    print new_row
                    writer.writerow(new_row)
                 
                
               except :
                                print("Oops!  That was no valid number.  Try again...")    
                    
out.close()
        
