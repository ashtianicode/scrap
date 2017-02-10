    # -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 19:33:37 2016

@author: taha
"""
import csv

l = ['www', 'poloto']

out = open('outtest.csv', 'w')
for row in l:
        out.write('%s;' % row)
        out.write('\n')
out.close()