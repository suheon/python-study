# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a

# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 예제 1
from random import randint
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
# print(dir(f))
f.close()

print('================================')
print('================================')

# 예제 2 (close 없이 with 끝나면 close )
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)


print('================================')
print('================================')

# 예제 3
with open('./resource/review.txt', 'r') as f:  # 한줄씩.
    for c in f:
        print(c.strip())


print('================================')
print('================================')
# 예제 5
with open('./resource/review.txt', 'r') as f:  # 한줄씩.
    line = f.readline()
    # print(line)
    while line:
        print(line, end="")
        line = f.readline()

print()

print(randint(3, 10))

l = range(6)
print(list(l))

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
list = ['Kim\n', "Park\n", "Cho\n"]
with open('./resource/text3.txt', 'w') as f:
    f.writelines(list)
