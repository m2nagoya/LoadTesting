# Locust

## 1. シナリオ開発の環境要件
|        |  公式doc | 本環境 |
| :----: | :-------: | :----: |
| **pypi** | 1.4.1 | 20.0.2 |
| **python** | 3.6 \| 3.7 \| 3.8 \| 3.9 | 3.8.3 |
  - Pythonが編集出来ればOS不問
  - VSCodeであれば中規模の開発において動作が軽快です(今回はViを使用)
    
## 2. シナリオ実行の環境要件(10,000 userによる 50,000 request per min)
- ### 実行端末  
| OS  | macOS Catalina 10.15.2 |  
| :----: | :-------: |  
| **CPU** | **1.4GHz クアッドコアIntel Core i5** |  
| **RAM** | **8GB 2133MHz LPDDR3** |  
- ### 実行要件  
| 最大ユーザ数<br>(Number of total users to simulate) |  1,000   |
| :----: | :-------: |
| **接続数の増加率<br>(Hatch rate)** |  **10**    |
| **アクセス先URL<br>(Host)** | http://localhost:8080 |

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

## 6. ログ
- ### 実行端末 / 実行要件
| OS  | macOS Catalina 10.15.2 | 最大ユーザ数<br>(Number of total users to simulate) |  10,000   | 
| :----: | :-------: | :----: | :-------: |
| **CPU** | **1.4GHz クアッドコアIntel Core i5** | **接続数の増加率<br>(Hatch rate)** |  **5**    |
| **RAM** | **8GB 2133MHz LPDDR3** | **アクセス先URL<br>(Host)** | http://localhost:8080 | 

![total_requests_per_second_1606451542](https://user-images.githubusercontent.com/51310989/100414108-4be1b480-30bc-11eb-8e85-d03b4b452d28.png)
![response_times_(ms)_1606451542](https://user-images.githubusercontent.com/51310989/100414110-4e440e80-30bc-11eb-84b8-bc8457b3efa6.png)
![number_of_users_1606451542](https://user-images.githubusercontent.com/51310989/100414112-4f753b80-30bc-11eb-8111-240d34a6bf7e.png)
