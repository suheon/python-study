# Section07-2
# 파이썬 클래스 상속 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

class Car:
    """ Parent class """

    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return "Car class 'show Method!' "


class BmwCar(Car):
    "Sub Class"

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s " % self.car_name


class BenzCar(Car):
    "Sub Class"

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s " % self.car_name

    def show(self):
        print(super().show())
        return 'Benz Card show method'


print("Class class")

# 일반 사용

model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color)  # super
print(model1.type)  # super
print(model1.car_name)

print(model1.show())

# Method Overriding (오버라이딩)
model2 = BenzCar('220d', 'suv', 'black')
print(model2.show())

# Parent Method Call
model3 = BenzCar('350s', 'sedan', 'silver')
print(model3.show())

# Inheritance Info
print(BmwCar.mro())  # 상속 정보를 리스트 형태로 반환  MRO (Method Resolution Order)


class X():
    pass


class Y():
    pass


class Z():
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(B.mro())
print(M.mro())
