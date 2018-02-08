#!/usr/bin/python
#coding:utf-8
import codecs
import requests  
from bs4 import BeautifulSoup
import random
import time
import csv
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()

# 对html进行解析
def paramAnalysis( item ):
    listSingle = []

    personStar = item.string
    personCommit = item.parent.contents[3].string

    soup1 = item .findParent('div',attrs={'class','mod'})
    
    allStars = soup1.find('strong',attrs={'class','rating_num'}).string
    moiveName = soup1.find('div',attrs={'class','title'}).find('a').string

    listSingle.append(personStar)
    listSingle.append(personCommit)
    listSingle.append(allStars)
    listSingle.append(moiveName)

    return listSingle


# 从cookies.txt中读取cookies
f=open('cookies.txt','r')
cookies={}
for line in f.read().split(';'):  
    name,value=line.strip().split('=',1)  
    cookies[name]=value 



# 读取输入的作为用户账号
# captcha = raw_input('please input the params:')
for j in range (0,1000):

    

    captcha = random.randint(10000000,99999999)

    url = "https://www.douban.com/people/%s/statuses"%(captcha)
    # url = "https://www.douban.com/people/34316735/statuses"

    print url

    # 使用已经登陆的cookie进行操作
    res=requests.get(url,cookies=cookies)  
    # print res.content

    # save_to_file('mobiles.txt', res.text)

    page = res.text
    soup = BeautifulSoup(page,"html.parser")
    result = soup.findAll('span',attrs={'class':'rating-stars'})

    print len(result)
    listAll = []
    for item in result:
        listAll.append(paramAnalysis(item))

    # 判断时候需要下一页
    pageLen = soup.find('span',attrs={'class':'thispage'})
    if pageLen is not None: 
        pageLenInfo = int(pageLen['data-total-page'])

        if pageLenInfo > 2:
            for i in range (2,pageLenInfo + 1):

                nextUrl = url + "?p=" + bytes(i) 
                nextRes=requests.get(nextUrl,cookies=cookies)

                nextPage = nextRes.text
                nextSoup = BeautifulSoup(nextPage,"html.parser")

                nextResult = []
                nextResult = nextSoup.findAll('span',attrs={'class':'rating-stars'})
                for item in nextResult:            
                    listAll.append(paramAnalysis(item))

    print listAll        

    if listAll:
        with open(bytes(captcha) + ".csv","w") as csvFile:
            csvFile.write(codecs.BOM_UTF8)
            writer = csv.writer(csvFile,dialect='excel')
            writer.writerow(["个人星级","个人评论","总星级","电影名称及时间"])
            writer.writerows(listAll)