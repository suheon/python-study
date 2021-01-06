# Section12-1
# 파이썬 데이타페이스 연동(SQLite)
# 테이블 생성 및 생성

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print(now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

print('sqlite version3 : ', sqlite3.version)
print('sqlite.sqlite_version : ', sqlite3.sqlite_version)
