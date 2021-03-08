# *args, **kwargs потребляеют все остальные аргументы
# def summ(a, b=5, *args, **kwargs):
#     return a + b + sum(args)
#
# res = summ(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(res)
#передавать аргументы можно позиционно или по ключу
# def summ(a, b=3):
#     return a + b
#
# res = summ(a=1, b=2)#передача аргумента по ключу, возможно
# print(res)#менять местами сам порядок аргументов

# def summ(a, b=2, *args, **kwargs):
#     return a + b
#
# res = summ(1, 2, 3, 4, 5, 6, 7, c=10, d=15)
# print(res)

# как посчитать сумму любой длинны строки с помощью *args
def my_sum(*args):
    res = 0
    for i in args:
        res += i
    return res

print(my_sum(1, 2, 3, 4, 5, 6, 7, 8))







