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

def getData(ulist,html):
    soup = BeautifulSoup(html, 'lxml')
    n=[0 for i in range(2)]
    for k in soup.find_all('div', class_="ch-tab clearfix"):
        u = k.find_all('a')
        for i in u:
            n[1]+=1
        n[0] += 1
    m=[[0 for i in range(n[0])]for i in range(n[1])]
    p=0
    q=0
    a=['硕士专业','博士专业']
    for k in soup.find_all('div', class_="ch-tab clearfix"):
        ulist = k.find_all('a')
        for i in ulist:
            m[p][1]=a[q]
            m[p][0]=i.string
            #print(m[p][0])
            #print(m[p][1])
            p+=1
        q+=1
    ulist=m
    #print(ulist)
    # return n[1]
def test(html):
    n=0
    soup = BeautifulSoup(html, 'lxml')
    for k in soup.find_all('div',class_='item-content js-current-item'):
        c=k.find_all('li')
        for i in c:
            n+=1
    # m = [[0 for i in range(6)] for i in range(n)]
    m = []
    p = 1
    q = 0
    major = ['硕士专业', '博士专业']
    for k in soup.find_all('div',class_='zx-yx-header'):
        c=k.find_all('h1')
        uni=c[0].text[:-1]
    ulist = []
    for k in soup.find_all('div', class_="ch-tab clearfix"):
        ulist = ulist + k.find_all('a')
        udiv = soup.find_all('div', class_="item-content js-current-item")
    for i, s in zip(ulist, udiv):
        a = s.text
        v = re.sub("\s+", "", a).split("]")
        # print(i.string)
        # m[p][0] = p + 1
        # m[p][1] = uni
        # m[p][2] = major[q]
        # m[p][3] = i.string
        for j in v[:-1]:
            j_sp = j.split("[")
            m.append([str(p)] + [str(uni)] + [i.string] + j_sp[:1] + j_sp[1:])
            # print(uni)
            # print(j_sp)
            # print(123)
            # +str(uni) + str(major[q])
            p+=1
        # print(456)
        #q+=1
    for k in m:
        print(k)

    #             m[p][4] = j_sp[0]
    #             m[p][5] = j_sp[1]
    #             m[p][0] = p + 1
    #             m[p][1] = uni
    #             m[p][2] = major[q]
    #             m[p][3] = i.string
    #             print(m[p][4])
    #             print(p)
    #             p+=1
    # q+=1
    # ulist = m
    # print(ulist)
            # v = a.strip()
            # c = re.split('\[', v[:-1])
            # print(v[:-1])
            # c = re.sub(r"\s+","", v[:-1])
            # print(c)
            # print(v)
        # for s in udiv:
        #     print(s.text)

    # z_test = zip(ulist, udiv)
    # print(z_test)


        # print(ulist)
        # print(soup.find_all('div', class_="item-content js-current-item"))
        # break
        # for i, s in zip(ulist, soup.find_all('div', class_="item-content js-current-item")):
        #     print(i, s)
        # #     slist = s.find_all('li')
        #     for x in slist:
        #         a = x.text
        #         v = a.strip()
        #         c = re.split('\[', v[:-1])
        #         print(c)
        #         print(m)
        #         print(p)
        #         m[p][4] = c[0]
        #         m[p][5] = c[1]
        #         m[p][0] = p + 1
        #         m[p][1] = uni
        #         m[p][2] = major[q]
        #         m[p][3] = i.string
        #         # print(1)
        #         # print(m)
        #         # print(len(m))
        #         # print(p)
        #         # print(m[p][2])
        #         # print(m[p][3])
        #         p += 1
        #
        #         #print(c[0])
        #         #print(p)
        # q += 1
        # print(123)
            #p+=1

    #ulist=m
    #print(m)

# def formatString2Array (string):
#     c= len(string)-1
#     a=re.split("【",string[:-1])
#
#     b=re.string.format(0, string.len() - 1).split('【')
#     print(a)




def main():
    uinfo=[]
    url = "https://yz.chsi.com.cn/sch/listYzZyjs--schId-368479,categoryId-692177275.dhtml"
    f = requests.get(url, headers=get_agent())
    f.raise_for_status
    f.encoding = f.apparent_encoding
    #getData(uinfo,f.text)
    test(f.text)
main()

