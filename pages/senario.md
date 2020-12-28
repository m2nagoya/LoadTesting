# マルチユーザPOSTシナリオ

## 1. プログラム
```
# cording: utf-8
import csv
import pprint
import json
import requests
import random
import string
import os
from locust import HttpLocust, TaskSet, task, HttpUser

url = 'http://127.0.0.1:5000/post'
companyID = 1234567890
limit = 3
w = 1

# CSV作成
def make_csv() :
    # loginnameとpasswordが入力されたCSVを作成
    if os.path.exists('profile.csv'):
        os.remove('profile.csv')

    with open('profile.csv', 'a', newline="") as f:
        writer = csv.writer(f)

        # ログインネームとパスワードを10000行出力
        for _ in range(10000):
            loginname = random.randint(10000,99999)
            password  = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])
            writer.writerow([loginname, password])

    # 単語が入力されたCSVを作成
    if os.path.exists('text.csv'):
        os.remove('text.csv')

    with open('text.csv', 'a', newline="") as f:
        writer = csv.writer(f)

        # 辞書から単語列を全て取得
        with open('/usr/share/dict/words','r', newline='') as f:
            lines = f.readlines()

        # 単語を10000行出力
        for _ in range(10000):
            text = lines[random.randint(1,len(lines)-1)].replace('\r\n','').replace('\n','')
            writer.writerow([text])

# CSV読み込み
def read_csv() :
    arr = []
    idx = random.randint(1, 10000)
    with open('profile.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if reader.line_num == idx:
                arr.append(row[0]) # loginname
                arr.append(row[1]) # password
                break
    with open('text.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if reader.line_num == idx:
                arr.append(row[0]) # text
                break
    return arr

class UserBehavior(TaskSet):
    make_csv() # 1度のみ実行

    @task(1)
    def get_param(self):
        self.loginname, self.password, self.text = read_csv()

    @task(1)
    def profile(self):
        self.client.post(url, {
                                "authInfo":{
                                    "companyId": companyID,
                                    "loginName": self.loginname,
                                    "password":  self.password
                                },
                                "resultRange":{
                                    "limit":limit
                                },
                                "searchCondition":{
                                    "text": self.text
                                }
                            }
                        )

class WebsiteUser(HttpUser):
    tasks = {UserBehavior:1}
    min_wait = w - 0.5 * w * random.gauss(0, 1)
    max_wait = w + 0.5 * w * random.gauss(0, 1)
```

## 実行結果
[実行結果(2020年12月28日)](https://github.com/m2nagoya/LoadTesting/blob/main/log/report_1609121213.8134851.html)




