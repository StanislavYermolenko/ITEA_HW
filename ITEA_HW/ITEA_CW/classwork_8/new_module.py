# import modules
# import calc
# q = modules.example(5)
# w = calc.my_sum(7, 13)
# print(q)
# print(w)

# #импортируем конкретную функцию pi из модуля math,
# # под именем N но выполняется
# # весь модуль, у нас есть доступ только к pi
from math import pi as N
a = 5 * N
print(a)

from my_package.f import bar


if __name__ == '__main__':
    bar()

