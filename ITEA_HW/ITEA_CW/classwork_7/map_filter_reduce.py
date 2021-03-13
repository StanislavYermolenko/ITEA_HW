# функции высшего порядка, аргументом принимают
# другую функцию, map первым аргументом принимает
# функцию, вторым коллекцию, возвращая при этом
# новую коллекцию, где она применила эту функцию
# на каждый елемент этой коллекции
# a = map(lambda i: i + 1, [1, 2, 3] )
# print(list(a))

# convert = map(lambda x: x ** 2, range(10))
# print(convert)  # возвращает объект функции
# print(list(convert))

# def example(q):
#     return q - 1
#
#
# q = map(example, [1, 2, 3, 4])
# print(list(q))

# filter принимает функцию и аргумент, однако
# в этом случае функция должна возвращать правдивое
# значение True, конструируя новый объект
# a = filter(lambda x: x >= 0, [1, -1, -5, 3, 7, -4])
# print(a)
# print(list(a))


# в функциональных языках программирования reduce и рекурсия
# заменяют циклы, вообще любое итерирование можно
# реализовать с reduce
#reduce превращает нашу коллекцию в любой возможный объект
#reduce задаются следующие аргументы:
# функция (lambda x, acc: acc + x), которая обязательно
#должна принимать два аргумента x, acc и возвращать
#одно значение acc + x
# коллекция [1, 2, 3]
# стартовое значение аккумулятора 0
from functools import reduce
a = reduce(lambda x, acc: acc + x, [1, 2, 3], 0)
print(a)
# как работает reduce - на первой итерации reduce
# посредством аргумента х берет
# стартовое значение аккумулятора, это 0 и первый
# аргумент из списка(нулевой), это 1 и передаст их
# функции, в нашем случае это сложение acc + x, 0 + 1
# получается 1, теперь эта единица становиться аккумулятором
# соответственно, на след итерации reduce берет второй
# елемент и текущее значение аккумулятора, которое сейчас
# равно 1 и прибавляет второе значение, равное 2. Получаем
# число 3 и записываем его в аккумулятор. Затем рекурсивно
# берем следующее значение равное 3 и прибавляем acc + x
# получаем число 6
# ВАЖНО! если мы не указываем начальное значение аккумулятора,
# reduce принимает за него нулевой элемент коллекции,
# a = reduce(lambda x, acc: acc + x, [1, 2, 3])
# в данном случае это цифра 1, получается на один шаг меньше





