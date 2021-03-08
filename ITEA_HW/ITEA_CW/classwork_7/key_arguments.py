# ключевые аргументы, есть стандартное значение b=5
def summ(a, b=5):
    return a + b
# если мы передаем в вызове второй аргумент, функция отрабатывает
# с ним, если нет, то тогда включается обязательный аргумент
res = summ(1)
print(res)
#сначала всегда идут позиционные аргументы
def my_func(country='Ukraine'):
    print('Im from ' + country)

my_func('Germany')
my_func('USA')
my_func()
