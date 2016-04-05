#!/usr/bin/env python
# -*-coding:utf-8 -*-

import urllib2
from bs4 import BeautifulSoup


def find_tag(soup, tag, attr):
    funcs = soup.find_all(tag, class_=attr)
    for func in funcs:
        print func.get_text()


def find_desc(soup, para_tag, tag):
    print soup.find(para_tag).find(tag)


if __name__ == "__main__":
    module = "mysql"
    url = "https://docs.saltstack.com/en/latest/ref/modules/all/salt.modules.%s.html"
    url = url %module
    request = urllib2.Request(url)
    request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)" \
                                    " Chrome/49.0.2623.75 Safari/537.36")
    response = urllib2.urlopen(request)
    if response.getcode() != 200:
        print("open %s error" %url)
        exit(2)
    content = response.read()
    soup = BeautifulSoup(content, 'html.parser', from_encoding="utf-8")
    # soup tag attr
    find_tag(soup, "code", attr="descname")
    #find_desc(soup, "dd","p")