# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import redis

r= redis.StrictRedis(host='localhost',port=6379, db=0)

captchas = r.keys()

for captcha in captchas :
    print "%s:%s" % (r.get(captcha), captcha)
