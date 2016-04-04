#!/usr/bin/env python
# -*-coding:utf-8 -*-

import urllib2

url = "http://www.baidu.com"

print("第一种方法")
response = urllib2.urlopen(url)
print(response.getcode())
print(len(response.read()))

print("第二种方法")
request = urllib2.Request(url)
request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36")
response = urllib2.urlopen(request)
print(response.getcode())
print(len(response.read()))

import cookielib
print("第三种方法")
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response = urllib2.urlopen(url)
print(response.getcode())
print(cj)
print response.read()