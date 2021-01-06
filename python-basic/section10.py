# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로는 에러가 없지만, 런타임프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크


# SyntaxError : 잘못된 문법

# print('Test)'

# NameError : 참조변수 없음

# ZeroDivisionError : 0 나누기 에러

# IndexError : 인덱스 범위 오버

# KeyError

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 에러.

# ValueError : 참조 값이 없을 때 발생

x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFoudError

# TypeError

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장 (EAEP 코딩 스타일)

# 예외 처리 기본
# try : 예외가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제1

name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    x = name.index(z)
    print("{} Found it {}! in name.".format(z, x+1))
# except ValueError:
except:
    print("Not Found it!")
else:
    print('OK! else!')


# 예제 3


name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim11'
    x = name.index(z)
    print("{} Found it {}! in name.".format(z, x+1))
# except ValueError:
# except Exception:
except Exception as e:
    print("Not Found it!")
    print('--------')
    print(e)
    print('--------')
else:
    print('OK! else!')
finally:
    print("OK")

# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('Try')
finally:
    print("finally")


# 예제 6
# 예외 발생 : raise
# raise 키워드롤 예외 직접 발생

try:
    a = 'Kim11'
    if a == 'Kim':
        print('Ok 허가!!')
    else:
        raise ValueError
except ValueError:
    print('VauleError')
