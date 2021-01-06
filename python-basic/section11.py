# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import pandas as pd
import csv

with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    print(type(reader))
    print(dir(reader))
    print()
    next(reader)  # Header 스킵

    for c in reader:
        print(c)


# 예제 2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')
    print(type(reader))
    print(dir(reader))
    print()
    next(reader)  # Header 스킵

    for c in reader:
        print(c)


# 예제 3 (Dict 변환)
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)
    # print(type(reader))
    # print(dir(reader))
    # print()
    # next(reader)  # Header 스킵

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('--------------')


# 예제 4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

with open('./resource/exm.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    # wt.writerows(w)
    for v in w:
        wt.writerow(w)


# 예제 5

# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils

# pandas 를 주로 사용 (openpyxl, xlrd)
# pip install xlrd
# pip install openpyxl
# pip install pandas


# sheetname='시트명' 또는 숫자, header=숫자, skiprow=숫자
xlsx = pd.read_excel('./resource/sample.xlsx')

print(xlsx.head())
print(xlsx.tail())

print(xlsx.shape)   # 행, 열

# 엑셀 or CSV 파일 쓰기

xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)
