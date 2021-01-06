# wikidocs/7022

string = 'abcdfe2a354a32a'

print(string.replace('a', 'A'))

string = 'abcd'
string.replace('b', 'B')
print(string)

a = "3"
b = "4"
print(a + b)


name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print("이름 : %s 나이 %d" % (name1, age1))
print("이름 : %s 나이 %d" % (name2, age2))


print("이름 : {} 나이 {}".format(name1, age1))


print(f"이름 : {name1} 나이 {age2}")

분기 = "2020/03(E) (IFRS연결)"

print(분기.split('(')[0])

print(분기[:7])


# box-sizing : border-box padding, border 까지 합이 width 로.

# 마진 상쇄, , 맞다은 box중 큰것으로.. 수직방향에서 마진 병합 현상이 일어난다.

# position : absolute 는 부모 중에 position: static 이 아닌 부분까지 거슬로 올라간다.

# id 선택자 > 클래스 선택자 > 태그 선택자

print("BTC_KRW".lower())

print("hello".capitalize())

file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))
print()
print(file_name.endswith(('xlsx', 'xls')))

file_name = "2020_보고서.xlsx"
print()
print(file_name.startswith('2020'))

a = "hello world"

print(a.split(' '))

movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

movie_rank.insert(1, '배트맨')

print(movie_rank)
