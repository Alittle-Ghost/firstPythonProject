import xlrd
from bs4 import BeautifulSoup
from xlutils.copy import copy
import requests
import re
import xlwt
import os
import io
import sys
import xlsxwriter as xw
import random

def get_agent():
   agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
             'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
   fakeheader = {}
   fakeheader['User-agent'] = agents[random.randint(0, len(agents)-1)]
   return fakeheader

def createExcel():
    workbook=xw.Workbook("info.csv")
    sheet1=workbook.add_worksheet("sheet1")
    sheet1.activate()
    title=['序号','院校名称','专业名称','方向名称','方向代码']
    sheet1.write_row('A1',title)
    workbook.close()

def getData(html):
    soup = BeautifulSoup(html, 'lxml')
    m = []
    p = 1
    q = 0
    major = ['硕士专业', '博士专业']
    for k in soup.find_all('div', class_='zx-yx-header'):
        c = k.find_all('h1')
        uni = c[0].text[:-1]
    ulist = []
    # u=['u']
    i=0
    h=0
    g=0
    y=0
    for k in soup.find_all('div', class_="ch-tab clearfix"):
        u = k.find_all('a')
    for i in u:
        g+=1
    for k in soup.find_all('div', class_="ch-tab clearfix"):
        ulist = ulist + k.find_all('a')
        udiv = soup.find_all('div', class_="item-content js-current-item")
    for i, s in zip(ulist, udiv):
        a = s.text
        v = re.sub("\s+", "", a).split("]")
        h+=1
        for j in v[:-1]:
            j_sp = j.split("[")
            if h<=g:
                m.append([str(p)] + [str(uni)] + [str(major[0])] + [i.string] + j_sp[:1] + j_sp[1:])
            else:
                m.append([str(p)] + [str(uni)] + [str(major[1])] + [i.string] + j_sp[:1] + j_sp[1:])
            p += 1
    # print(m)
    w_str = ""
    for n in m:
        w_str = w_str + ",".join((n)) + "\n"
    with open("info1.csv", "w", encoding="utf-8") as f:
        f.write(w_str)
    # wb.save("info.csv")

def main():

    url = "https://yz.chsi.com.cn/sch/listYzZyjs--schId-368479,categoryId-692177275.dhtml"
    f = requests.get(url, headers=get_agent())
    f.raise_for_status
    f.encoding = f.apparent_encoding
    # createExcel()
    getData(f.text)

main()




