#номер элемента ряда Фибоначчи
# 1 1 2 3 5 8 13 21
# def fibo(n):
#     if n <= 2:
#         return 1
#     return fibo(n - 2) + fibo(n - 1)
#
#
# print(fibo(1))
# print(fibo(2))
# print(fibo(3))
# print(fibo(4))
# print(fibo(5))
# print(fibo(6))
# print(fibo(7))
# print(fibo(8))

# 5! = 5 * 4 * 3 * 2 * 1
def fact(num):
    if num == 1:
        return 1
    return num * fact(num - 1)
#вызовы идут в глубину до базового случая, затем цепочка
#сврачивается наверх, возвращая значения

