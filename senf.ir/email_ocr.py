# -*- coding: utf-8 -*-
import csv
import cv2
import os

import sys
reload(sys)
sys.setdefaultencoding('utf8')




numberofnoemails=0
numberofemails=0
loop =0
with open('test_output.csv', 'rb') as csvfile:
                      reader = csv.DictReader(csvfile)
                      for row in reader:   
                             import doc2text
                             doc = doc2text.Document()
                             doc = doc2text.Document(lang="eng")
                             loop = loop +1 
                             email_img_url =  row['email']
                             if email_img_url != '0' :
                                 
                                      try:                                  
                                           numberofemails = numberofemails +1
                                           email_img_folder='/home/taha/Documents/playground/senf.ir/big_version_file/'
                                           big_version_name='big_'+email_img_url
                                           img =os.path.join(email_img_folder, big_version_name)
                                           doc.read(img)
                                           doc.process()
                                           doc.extract_text()
                                           text = doc.get_text()
                                           print loop,text
                                           text=''
                                           my_dict = {loop:['a','b',text]}
                                           with open('mycsvfile.csv', 'wb') as f:  # Just use 'w' mode in 3.x
                                                    w = csv.DictWriter(f, my_dict.keys())
                                                    w.writerow(my_dict)

                                      except:
                                           print ''
                                  
                             else: 
                                 numberofnoemails = numberofnoemails + 1
                      print 'number of data having emails : ',numberofnoemails 
                      print 'number of data dont have any email : ',numberofemails           




