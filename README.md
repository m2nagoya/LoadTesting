# Locust

- シナリオ開発の環境要件
    |        |  公式doc | 本環境 |
    | :----: | :-------: | :----: |
    | **pypi** | 1.4.1 | 20.0.2 |
    | **python** | 3.6 \| 3.7 \| 3.8 \| 3.9 | 3.8.3 |

- シナリオ実行の環境要件 <br> (シナリオ基本要件　10,000 userによる 50,000 request per min)
    | 最大ユーザ数<br>(Number of total users to simulate)|  10,000   |
    | :----: | :-------: |
    | **接続数の増加率<br>(Hatch rate)** |  **5**    |
    | **アクセス先URL<br>(Host)** | http://localhost:8080 |

- 実行結果の可視化はイケてるか
![total_requests_per_second_1606451542](https://user-images.githubusercontent.com/51310989/100414108-4be1b480-30bc-11eb-8e85-d03b4b452d28.png)
![response_times_(ms)_1606451542](https://user-images.githubusercontent.com/51310989/100414110-4e440e80-30bc-11eb-84b8-bc8457b3efa6.png)
![number_of_users_1606451542](https://user-images.githubusercontent.com/51310989/100414112-4f753b80-30bc-11eb-8111-240d34a6bf7e.png)

- 他の負荷試験ツールにもっといいのがすぐ見つかるか？
  - JMeter
    - 豊富なレポートや複雑なシナリオを書くことが可能  
    - 古くからあるため情報が沢山ある  
    - メモリ管理が面倒(たまに落ちる)  
  - Gatling
    - 豊富なレポートや複雑なシナリオを書くことが可能  
    - Scalaでシナリオを書ける

  \[参考\] <br> https://speakerdeck.com/nissy0409240/pythondeshi-merufu-he-shi-yan?slide=13

- 第一印象で嫌なところ、イケてないところがあるか？
  - 機能が少ないように感じた。 
