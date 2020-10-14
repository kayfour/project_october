import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


db_url = 'mongodb://127.0.0.1:27017/'
url = "https://www.k-startup.go.kr/common/announcement/announcementList.do?mid=30004&bid=701&searchAppAt=A"
#header = {'Referer' :'https://movie.daum.net/premovie/released',
#            'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
res = requests.get(url)#, headers = header) 
						        # shared github
soup = BeautifulSoup(res.content, features='lxml')


for i in soup.select('#liArea12 > h4 > a'):
    s.append(t)
    
print(s)    
