# генераторные выражения генерируют коллекцию на ходу
a = [x ** 2 for x in range(10)]
print(a)
# можно внутри устанавливать фильтры
b = [x ** 2 for x in range(10) if x > 3 and x % 2 == 0]
print(b)

c = {key: val for key, val in enumerate(range(2, 10))}
print(c)

d = (x for x in range(10))
print(d)#объект генератора

e = tuple(x for x in range(10))
print(e)#генерация кортежа

f = [(x, y) for x in range(5) for y in range(5, 10)]
print(f)

