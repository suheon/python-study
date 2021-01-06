# Section13

# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time
import winsound
import datetime
import sqlite3

conn = sqlite3.connect(
    "D:/WORKSPACE/python-study/resource/records.db", isolation_level=None)

# Cursor 연결
cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS records ( \
      id INTEGER PRIMARY KEY AUTOINCREMENT, \
      cor_cnt INTEGER, \
      record text, \
      regdate text )\
")


words = []  # 영어 단어 리스트 (1000개 로드)

n = 1  # 게임시도 횟수
cor_cnt = 0  # 정답개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

# print(words)

input("Ready? Rress Enter Key!")  # Enter game start

start = time.time()

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)

    print()

    print("*Question # {}".format(n))
    print(q)

    x = input()  # 타이핑 입력

    print()

    if str(q).strip() == str(x).strip():
        print("Pass!")
        cor_cnt += 1
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
    else:
        print("Wrong!")
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
    n += 1

end = time.time()

et = end - start
et = format(et, ".3f")

print()
if cor_cnt >= 3:
    print('합격')
else:
    print('불합격')

cursor.execute("INSERT INTO records(cor_cnt, record, regdate) values (?, ?, ?) ",
               (cor_cnt, et, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
               )

print("게임시간 : ", et, "초", "정답개수 : {}".format(cor_cnt))

# if __name__ == '__main__':
#     pass
