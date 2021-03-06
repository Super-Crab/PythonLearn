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


pageNum = 200

# 读取输入的作为用户账号
# captcha = raw_input('please input the params:')
for j in range (0,100):

    pageNum += 20
    captcha = random.randint(1000000,9999999)
    url_user = "https://movie.douban.com/subject/20326665/reviews?start=%s"%(pageNum)

    print url_user

    # 使用已经登陆的cookie进行操作
    res_user=requests.get(url_user,cookies=cookies)  
    # print res.content

    page_user = res_user.text
    soup_user = BeautifulSoup(page_user,"html.parser")
    result = soup_user.findAll('a',attrs={'class':'avator'})

    for item in result:
        print item['href'].split('/')[4]

        
        captcha = item['href'].split('/')[4]

        tim = random.randint(8,13)
        print 'sleep tim = '+ bytes(tim)
        time.sleep(tim)

        

        url = "https://www.douban.com/people/%s/statuses"%(captcha)
        # url = "https://www.douban.com/people/34316735/statuses"

        print url

        # 使用已经登陆的cookie进行操作
        res=requests.get(url,cookies=cookies)  
        # print res.content

        # save_to_file(bytes(captcha)+'.txt', res.text)

        page = res.text
        soup = BeautifulSoup(page,"html.parser")
        result = soup.findAll('span',attrs={'class':'rating-stars'})

        # 经抓包发现 豆瓣存在两种用户的评论  一种必须有星级  一种没有  此处取必须有星级的
        if result is not None:

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

                        print 'current page = ' + bytes(i) + ' page count = ' + bytes(pageLenInfo + 1)

                        nexttim = random.randint(8,13)
                        print 'sleep tim = '+ bytes(nexttim)
                        time.sleep(nexttim)
                        
                        nextUrl = url + "?p=" + bytes(i) 
                        nextRes=requests.get(nextUrl,cookies=cookies)

                        nextPage = nextRes.text
                        nextSoup = BeautifulSoup(nextPage,"html.parser")

                        nextResult = []
                        nextResult = nextSoup.findAll('span',attrs={'class':'rating-stars'})
                        for item in nextResult:            
                            listAll.append(paramAnalysis(item))

            print '用户 ： '+ bytes(captcha) +' 总条数： '+len(listAll)        

            if listAll:
                with open(bytes(captcha) + ".csv","w") as csvFile:
                    csvFile.write(codecs.BOM_UTF8)
                    writer = csv.writer(csvFile,dialect='excel')
                    writer.writerow(["个人星级","个人评论","总星级","电影名称及时间"])
                    writer.writerows(listAll)