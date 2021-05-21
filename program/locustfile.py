# coding: utf-8

'''
ここは public repository なので example.com などで記述します。

POST /search/Search HTTP/1.1
Host: www.example.com
Content-Type: application/json
Cache-Control: no-cache

{"authInfo":{"companyId":1234567890,"loginName":"0123","password":"abcdefghijklmn"},"resultRange":{"limit":3},"searchCondition":{"text":"オーブン"}}

companyId は半固定（引数やpropertyで1つ与える）
(loginName, password)は別途CSVでN組を与える
resultRange.limit は 半固定（引数やpropertyで1つ与える）
searchCondition.text は別途CSVでM組を与える
各接続の各ループで、N組の認証CSVとM組のキーワードCSVからランダム選択して、バリエーションのばらけたPOST request で負荷試験してください。

負荷のかけ方のパラメータとしては下記の半固定パラメータも必要です

Hatch Rate
Max Connections
request間の平均wait (msec)
各ループ毎のwait は w +/- 0.5 * w * random でrequest間隔をばらつかせる。JMeterにあるガウス乱数だとうれしい。

実際の接続先につなぐには、いろいろと障壁があるので、ダミーサーバも作ってシナリオ開発してください。
'''

import csv
import pprint
import json
import requests
import random
import string
import os
import itertools
from locust import HttpLocust, TaskSet, task, HttpUser

url = 'http://127.0.0.1:5000/post'
companyID = 1234567890
limit = 3
w = 1     # wait_time

# csv読込(一括)
class read_csv :
    data = [] # [loginname, password, text]
    arr1, arr2, arr3 = [], [], []

    # 初期化
    def __init__(self):
        # それぞれ配列に格納
        with open('data/profile.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.arr1.append(row[0]) # loginname
                self.arr2.append(row[1]) # password
        with open('data/text.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.arr3.append(row[0]) # text

        # 個々の配列を統合
        for i, j, k in zip(self.arr3, self.arr2, self.arr1):
            self.data.append([i, j, k])
    
        # ランダム化
        random.shuffle(self.data)

        # イテレータに変換
        self.data = itertools.cycle(self.data)

instance = read_csv() # インスタンス生成

class UserBehavior(TaskSet):

    @task(1)
    def profile(self):
        loginname, password, text = next(instance.data)
        print(loginname, password, text)

        self.client.post(url, {
                                "authInfo":{
                                    "companyId": companyID,
                                    "loginName": loginname,
                                    "password":  password
                                },
                                "resultRange":{
                                    "limit":limit
                                },
                                "searchCondition":{
                                    "text": text
                                }
                            }
                        )

class WebsiteUser(HttpUser):
    tasks = {UserBehavior:1}
    min_wait = w - 0.5 * w * random.gauss(0, 1)
    max_wait = w + 0.5 * w * random.gauss(0, 1)
