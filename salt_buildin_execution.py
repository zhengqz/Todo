#!/usr/bin/env python
# -*-coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import xlwt
import re


from translate.google_api import get_translate_one



def write_excel(soup):
    file = xlwt.Workbook()
    table = file.add_sheet("salt", cell_overwrite_ok=True)

    all_modules = soup.find_all("tr", class_=re.compile("row-odd|even"))
    table.write(0, 0, "命令")
    table.write(0, 1, "功能")
    table.write(0, 2, "URL")
    row = 1
    for module in all_modules:
        # print module
        # https: // docs.saltstack.com / en / latest / ref / modules / all / salt.modules.cmdmod.html
        href = module.find("a", class_="reference internal").get("href").split("#")[0]
        name = module.find("span", class_="pre").get_text()
        comment = module.td.find_next_sibling("td").get_text()
        module_url = module_url_pre + href
        comment = get_translate_one(comment, "span", id="result_box")
        table.write(row,0,name)
        table.write(row,1,comment)
        table.write(row,2,module_url)
        row += 1
        print name, comment, module_url
    f_name = "%s.xls" %"salt"
    file.save(f_name)

if __name__ == "__main__":
    url = "https://docs.saltstack.com/en/latest/ref/modules/all/index.html"
    module_url_pre = "https://docs.saltstack.com/en/latest/ref/modules/all/"
    request = urllib2.Request(url)
    request.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36")

    response = urllib2.urlopen(request)
    if response.getcode() != 200:
        print("get url %s ERROR." % url)
        exit(1)
    content = response.read()
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    #  <a class="reference internal" href="salt.modules.aliases.html#module-salt.modules.aliases" title="salt.modules.aliases">
    #  <code class="xref py py-obj docutils literal"><span class="pre">aliases</span></code></a>

    write_excel(soup)


