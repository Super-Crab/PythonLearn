#!/usr/bin/python
#coding:utf-8

import requests  
from bs4 import BeautifulSoup
import csv
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()



f=open('cookies.txt','r')

cookies={}
for line in f.read().split(';'):  
    name,value=line.strip().split('=',1)  
    cookies[name]=value 


# captcha = raw_input('please input the params:')

# url = "https://www.douban.com/people/%s/statuses"%(captcha)
url = "https://www.douban.com/people/34316735/statuses"

print url

res=requests.get(url,cookies=cookies)  
# print res.content

# save_to_file('mobiles.txt', res.text)

page = res.text
soup = BeautifulSoup(page,"html.parser")
pageLen = soup.find('span',attrs={'class':'thispage'})

result = soup.findAll('span',attrs={'class':'rating-stars'})

print len(result)

#个人星级评分
listPersonStars = []
#个人评语
listPersonCommit = []
#总体的分数
listAllStars = []
#电影名字
listMoivesName = []

for item in result:

    personStar = item.string
    listPersonStars.append(personStar)
    print personStar

    personCommit = item.parent.contents[3].string
    listPersonCommit.append(personCommit)
    print personCommit

    soup1 = item .findParent('div',attrs={'class','mod'})
    
    allStars = soup1.find('strong',attrs={'class','rating_num'}).string
    listAllStars.append(allStars)
    print allStars

    moiveName = soup1.find('div',attrs={'class','title'}).find('a').string
    listMoivesName.append(listMoivesName)
    print moiveName




pageLenInfo = int(pageLen['data-total-page'])

if pageLenInfo > 2:
    for i in range (2,pageLenInfo + 1):
        nextResult = []
        print i
        nextUrl = url + "?p=" + bytes(i) 
        print nextUrl
        nextRes=requests.get(nextUrl,cookies=cookies)

        nextPage = nextRes.text
        nextSoup = BeautifulSoup(nextPage,"html.parser")

        nextResult = nextSoup.findAll('span',attrs={'class':'rating-stars'})
        print nextUrl
        for item in nextResult:

            personStar = item.string
            listPersonStars.append(personStar)
            print personStar

            personCommit = item.parent.contents[3].string
            listPersonCommit.append(personCommit)
            print personCommit

            soup1 = item .findParent('div',attrs={'class','mod'})
            
            allStars = soup1.find('strong',attrs={'class','rating_num'}).string
            listAllStars.append(allStars)
            print allStars

            moiveName = soup1.find('div',attrs={'class','title'}).find('a').string
            listMoivesName.append(listMoivesName)
            print moiveName

with open("1.csv","w") as csvFile:
     writer = csv.writer(csvFile)
     writer.writerow(["1","2","3","4"])
     writer.writerows([listPersonStars,listPersonCommit,allStars,listMoivesName])