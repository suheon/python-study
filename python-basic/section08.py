# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대경로


# 사용 1 (클래스)
import builtins
import pkg.prints as p
import pkg.calculations as c
from pkg.fibonacci import Fibonacci as Fib
from pkg.fibonacci import Fibonacci
from pkg.calculations import div as d

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))
print("ex1 : ", Fibonacci().title)

# 사용 2
# from pkg.fibonacci import * (저 파일 class 전부다 , 권장 하지 않음)

# 사용 3

Fib.fib(500)


print('ex4 : ', c.add(10, 100))
print('ex5 : ', int(d(100, 10)))

p.prt1()
p.prt2()

# print(dir(builtins))
