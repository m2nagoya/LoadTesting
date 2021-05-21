import csv
import random
import string
import os
import shutil

# csv作成
def make_csv() :
    shutil.rmtree('data')
    os.makedirs('data')

    # loginnameとpasswordが入力されたCSVを作成
    with open('data/profile.csv', 'a', newline="") as f:
        writer = csv.writer(f)

        # ログインネームとパスワード(5桁)を10000行出力
        for _ in range(10000):
            loginname = random.randint(10000,99999)
            password  = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])
            writer.writerow([loginname, password])

    # 単語が入力されたCSVを作成
    with open('data/text.csv', 'a', newline="") as f:
        writer = csv.writer(f)

        # 辞書から単語列を全て取得
        with open('/usr/share/dict/words','r', newline='') as f:
            lines = f.readlines()

        # 単語を10000行出力
        for _ in range(10000):
            text = lines[random.randint(1,len(lines)-1)].replace('\r\n','').replace('\n','')
            writer.writerow([text])

def main():
  make_csv()

if __name__ == "__main__":
  make_csv()
