# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import csv
import cv2
import os
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')



numberofnoemails=0
numberofemails=0
n_valid_emails=0
with open('100k_test_output.csv', 'rb') as csvfile:
                      reader = csv.DictReader(csvfile)
                      for row in reader:   
                             email_img_url =  row['email']
                             if email_img_url != '0' :
                                 
                                      try: 
                                           time.sleep(1)                                 
                                           numberofemails = numberofemails +1
                                           email_img_folder='/home/taha/Documents/playground/selenium/email_img/'
                                           img = cv2.imread(os.path.join(email_img_folder,email_img_url))
                                           big_version = cv2.resize(img, (0,0), fx=5, fy=5) 
                                           big_version_name='big_'+email_img_url
                                           cv2.imwrite(os.path.join('big_version_file', big_version_name),big_version)
                                           cv2.imshow('img',img)
                                           cv2.imshow('big_img',big_version)
                                           big_img_url=os.path.join('/home/taha/Documents/playground/senf.ir/big_version_file/',big_version_name)
                                           print big_img_url
                                           

                                      except:
                                           print 'oops'
                                           n_valid_emails = n_valid_emails+1
                                  
                             else: 
                                 numberofnoemails = numberofnoemails + 1
                      print 'number of data having emails : ',numberofnoemails 
                      print 'number of data dont have any email : ',numberofemails           
                      print 'not valid emails : ',n_valid_emails



