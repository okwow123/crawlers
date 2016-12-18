# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup
#url = 'http://cafe.daum.net/_c21_/recent_bbs_list?grpid=1UW9S&fldid=_rec' + str(1)
url='http://top.cafe.daum.net/_c21_/search?search_opt=name&sort_type=recent&q=%ED%94%84%EB%B0%94&search_type=tab'+str(1)
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'lxml')
index = 0
for link in soup.select('div > div > a'):
    #print link
    href=link.get('href')
    if href[0:20]=='http://cafe.daum.net':
        name = soup.find_all("a", class_="link_tit #cafename#result#name")
        date = soup.find_all("div", class_="info_scafe")
        print index
        print href       #address
        print name[index].get_text()#name 
        index2=date[index].get_text().index(': 201')+1
        print date[index].get_text()[index2:len(date[index].get_text())].strip()#opendate
        index+=1
