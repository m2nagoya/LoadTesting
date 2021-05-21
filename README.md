# Locust

## 1. シナリオ開発の環境要件
|        |  公式doc | 本環境 |
| :----: | :-------: | :----: |
| **pypi** | 1.4.1 | 20.0.2 |
| **python** | 3.6 \| 3.7 \| 3.8 \| 3.9 | 3.8.3 |
  - Pythonが編集出来ればOS不問
  - VSCodeであれば中規模の開発において動作が軽快です(今回はViを使用)
    
## 2. シナリオ実行の環境要件
- ### 実行端末  
| OS  | macOS Catalina 10.15.2 |  
| :----: | :-------: |  
| **CPU** | **1.4GHz クアッドコアIntel Core i5** |  
| **RAM** | **8GB 2133MHz LPDDR3** |  
- ### 実行要件  
| 最大ユーザ数<br>(Number of total users to simulate) |  1,000   |
| :----: | :-------: |
| **接続数の増加率<br>(Hatch rate)** |  **10**    |
| **アクセス先URL<br>(Host)** | http://127.0.0.1:5000 |

## 3. 実行結果の可視化はイケてるか
- ### 1秒毎のリクエスト数
  ![number_of_users_1606872790](https://user-images.githubusercontent.com/51310989/100818086-c0d23700-348c-11eb-8190-25af280edbaa.png)
- ### 1ms毎の応答時間
  ![response_times_(ms)_1606872790](https://user-images.githubusercontent.com/51310989/100818089-c3349100-348c-11eb-9b6a-b084ba457194.png)
- ### ユーザー数の推移
  ![total_requests_per_second_1606872790](https://user-images.githubusercontent.com/51310989/100818091-c3cd2780-348c-11eb-8c0b-5a1f0882cba2.png)
- ### locustで出力されるデータ
  - リクエストに関するステータス(CSV)
  - リクエスト失敗に関するログ(CSV)
  - 例外のStackTrace(CSV)
  - レポート(ステータス、可視化チャートなど)
- ### PNG形式で可視化チャートのダウンロード可能

## 4. 他の負荷試験ツールにもっといいのがすぐ見つかるか？
- ### JMeter
  - 豊富なレポートや複雑なシナリオを書くことが可能  
  - 古くからあるため情報が沢山ある  
  - メモリ管理が面倒(たまに落ちる)
  - プログラミング言語はJava
- ### Gatling
  - 豊富なレポートや複雑なシナリオを書くことが可能  
  - プログラミング言語はScala
- ### Tsung
  - 実行毎にシナリオ・ログを別ディレクトリに保存してくれる
  - HTMLのレポートを作れる
  - JSONで結果を取得
  - プログラミング言語はErlang

  \[参考\] <br> https://speakerdeck.com/nissy0409240/pythondeshi-merufu-he-shi-yan?slide=13

## 5. 第一印象で嫌なところ、イケてないところがあるか？
  - JMeterの場合、テストシナリオ、スレッドグループ、サンプラーなどリクエスト処理に細かなオプション設定があります
  - GUIではなくDockerを用いるためプログラミングスキルが必要(JMeterはGUI/CUI)

## 6. プログラム
```
# coding: utf-8

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
```

## 7. 実行方法
```
# イメージのダウンロード
docker pull centos:centos7 python:3.6

# docker起動
docker run -it -p 8089:8089 —name locust -d centos:centos7
docker exec -it locust /bin/bash

# ローカルからコンテナへデータ転送
docker cp post locust:post

# 文字化け対策
export LANG=en_US.UTF-8

# python3のインストール
yum install python3

# pip3のアップグレード
pip3 install —upgrade pip

# python ライブラリのインストール
pip3 install requests locust itertools

# locust 起動
locust --host=http://127.0.0.1:5000
```

## 8. 実行ログ
- [実行結果(2020年12月28日)](https://github.com/m2nagoya/locust/blob/main/log/report_1609121213.8134851.html)
- [実行結果(2021年5月21日)](https://github.com/m2nagoya/locust/blob/main/log/report_1621579564.4859762.html)
