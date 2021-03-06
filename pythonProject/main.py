from bs4 import BeautifulSoup
from lxml import html
import xml
import requests
import random


def get_agent():
   agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
             'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
   fakeheader = {}
   fakeheader['User-agent'] = agents[random.randint(0, len(agents))]
   return fakeheader

def get_html(url):
   try:
      r = requests.get(url, timeout=5,headers=get_agent())
      r.raise_for_status
      r.encoding = r.apparent_encoding
      return r.text
   except:
      return "Someting Wrong！"


print(get_html('https://yz.chsi.com.cn/sch/listYzZyjs--schId-368479,categoryId-692177275.dhtml'))

