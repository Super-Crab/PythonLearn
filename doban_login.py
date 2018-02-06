# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()

url =  'https://accounts.douban.com/login'
#构造post数据
data={
    'redir': 'https://www.douban.com',
    'form_email':'',
    'form_password':'',
    'login':'登录',
    'source':'None'
}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
r = requests.post(url, data, headers=headers)
page = r.text
#利用bs4获得验证码图片地址
soup = BeautifulSoup(page,"html.parser")
captcha_url = soup.find('img',id='captcha_image')['src']
#利用正则获得验证码ID
pattern = re.compile('<input type="hidden" name="captcha-id" value="(.*?)"/')
captcha_id = re.findall(pattern, page)
#将验证码图片保存到本地
urllib.urlretrieve(captcha_url,"captcha.jpg")
captcha = raw_input('please input the captcha:')
data['captcha-solution'] = captcha
data['captcha-id'] = captcha_id

r = requests.post(url, data=data, headers=headers)

save_to_file('mobiles.txt', r.text)

page = r
