#!/usr/bin/python
# coding:utf-8
import os
import json
import urllib3
import random
import time
import codecs
import csv


def saveFile(fileName, list):
    with open("1.csv", "w", encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile, dialect='excel')
        writer.writerows(list)


if __name__ == "__main__":
    nameList = []
    labelList = []
    head = {
        'accept': 'accept',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': '_gcl_au=1.1.1003123510.1547122313; csrftoken=iUHXgICttmBXn5ON2Pc0kyT1eCiEu2x5; SPC_IA=-1; SPC_EC=-; SPC_U=-; welcomePkgShown=true; bannerShown=true; SPC_F=BtwJdg2kkGUSWZGQ0srPT1y6jVUsyVhM; REC_T_ID=ed6217be-14d0-11e9-805e-52540007434f; SPC_T_ID="fsiJJC5KwkGseKxhYRGEaN4CxpyxJZj42MOWmPqfnm3hhCnnXDPx5ZNcM4lKPrc0KTD7ZLlAeNuGkxWuKMWlUJZeSlk2Avut40Njk3OvN1M="; SPC_SI=ni1htar7p4ynhpx2zv175doz7jxmbkbo; SPC_T_IV="z9YK9WpY3mIi200JdeYARg=="; language=en; _ga=GA1.3.633471432.1547122357; _gid=GA1.3.1563306221.1547122357',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    url = "https://shopee.com.my/api/v2/search_items/?by=pop&limit=20&match_id=2428&newest=0&order=desc&page_type=search"
    http = urllib3.PoolManager()
    response = http.request('GET', url, headers=head)
    data = json.loads(response.data.decode('utf-8'))
    print(data['items'])
    items = list(data['items'])
    for item in items:
        time.sleep(random.randint(3, 6))
        itemid = item['itemid']
        shopid = item['shopid']
        info_url = "https://shopee.com.my/api/v2/item/get?itemid=%d&shopid=%d" % (itemid, shopid)
        print(info_url)
        response = http.request('GET', info_url, headers=head)
        info_data = json.loads(response.data.decode('utf-8'))
        print(info_data)
        print(list(info_data['item']['hashtag_list']))
        print(info_data['item']['name'])
        nameList.append(info_data['item']['name'])
        itemLabel = list(info_data['item']['hashtag_list'])
        if itemLabel:
            for label in itemLabel:
                if label not in labelList:
                    labelList.append(label)

        if nameList:
            saveFile("title", nameList)
        if labelList:
            saveFile("label", labelList)
