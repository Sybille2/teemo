# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'

import httplib

conn = httplib.HTTPConnection('127.0.0.1',9988)
conn.request('GET',r'http://www.google.com')
r = conn.getresponse()
data = r.read()
print data