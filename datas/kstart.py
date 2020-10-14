import os 
import time
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

url = "https://www.k-startup.go.kr/common/announcement/announcementList.do?mid=30004&bid=701&searchAppAt=A"
res = requests.get(url=url)
soup = BeautifulSoup(res.content, features='lxml')

def DBinsert(data):
    db_url = 'mongodb://127.0.0.1:27017/'

    with MongoClient(db_url) as client:
        kdb = client['kstartup']
        infor = kdb.kdbCollection.insert_one(data)

def kdb():
       
    terms = soup.select('h4 > span[class*="ann_list_day"]')    
    cates = soup.select('h4 > span[class*="ann_list_group"]') 
    li1_text, li2_text, li3_text= [], [], []
    ul_tags = soup.find_all('ul', class_='ann_list_info m0')
    for ul in ul_tags:
        li_tags = []
        for li in ul.find_all('li'):
            li_tags.append(li.text)
        li1_text.append(li_tags[0])
        li2_text.append(li_tags[1])
        li3_text.append(li_tags[2].split()[1])

    titles= soup.select("li > h4 > a")
    for cate, term, title, li11_text, li22_text, li33_text in zip(cates, terms, titles, li1_text, li2_text, li3_text):
        data = {'Category':cate.text, 'Term':term.text, 'Title':title.text.strip(), 'sorting':li11_text, 'Company':li22_text, 'Due':li33_text}
        print(data)
        DBinsert(data)

if __name__ == "__main__":
    kdb()