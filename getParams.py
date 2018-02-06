import requests  
from bs4 import BeautifulSoup

f=open('cookies.txt','r')

cookies={}
for line in f.read().split(';'):  
    name,value=line.strip().split('=',1)  
    cookies[name]=value 
res=requests.get("https://www.douban.com/people/34316735/statuses",cookies=cookies)  
# print res.content

page = res.text
soup = BeautifulSoup(page,"html.parser")
result = soup.findAll('span',attrs={'class':'rating-stars'})

print len(result)

for item in result:
    print item.parent.contents[3].string