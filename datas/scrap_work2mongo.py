from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pymongo import MongoClient
import datetime

#path = '/home/cloudera/Documents/Develop/chromedriver'
chromedriver = '/home/cloudera/Documents/Develop/project_october/chromedriver'  
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.work.go.kr/empInfo/indRev/indRevMain.do')
ti = driver.find_element_by_xpath("/html//title") 
c_search=driver.find_element_by_xpath('//*[@id="empListInfoDiv"]/div[3]/p/strong').text
print (ti.get_attribute('text'))
print(c_search)
c=int(c_search)
j=1
dates = list()
while j < c:
    
    title = str()
    link = str()
    if j%10 != 0:
        l= str("list"+str(j%10))
        titl = driver.find_element_by_xpath(f'//*[@id="{l}"]/td[3]/div/div/a')
        title = titl.get_attribute('text') 
        ', python.'.strip(',.')
        title = title.strip('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t')  
        link =titl.get_attribute('href')
        
        data = {"title": title, "link": link, "create_date": datetime.datetime.now()}
        dates.append(data)
        print (data)
           
    elif j%10 ==0:
        titl = driver.find_element_by_xpath('//*[@id="list10"]/td[3]/div/div/a')
        title = titl.get_attribute('text')
        title = title.strip('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t')
        link =titl.get_attribute('href')
        data = {"title": title, "link": link, "create_date": datetime.datetime.now()}
        dates.append(data)
        print (dates)
        with MongoClient('mongodb://127.0.0.1:27017/')  as client:
            mydb = client.mydb
            res = mydb.work.insert_many(dates)
        elem = driver.find_element_by_xpath('//*[@id="currentPageNo"]')
               
        page = (j//10)+1
        print(dates)
        dates=[]
        print("page :",page)
        elem.clear()
        elem.send_keys(page)
        time.sleep(5)
        elem.send_keys(Keys.RETURN) 
        time.sleep(7)    
    
    j=j+1
         
    if j == c:
        break
    continue    

driver.quit()