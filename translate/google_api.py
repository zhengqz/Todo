#!/usr/bin/env python
# -*-coding:utf-8 -*-

import urllib2
import urllib
from bs4 import BeautifulSoup


# http://translate.google.cn/#en/zh-CN/hello

def get_translate_one(values, tag, **kargs):
    """
        puts value to translate en->ch
    """
    url = "http://translate.google.cn/#en/zh-CN/"
    query = values
    value = {"q": query}
    data = urllib.urlencode(value)
    request = urllib2.Request(url, data)
    request.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36")
    try:
        response = urllib2.urlopen(request)
        content = response.read()
        soup = BeautifulSoup(content, 'html.parser', from_encoding="utf-8")
        result = soup.find(tag, **kargs)
    except Exception, e:
        print(e)
        return
    return result.get_text()
