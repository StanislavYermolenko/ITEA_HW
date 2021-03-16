# import calc
# a = calc.my_sum(1, 6)
# print(a)
# если мы хотим импортировать функцию но не хотим чтобы
# выполнялся весь код в этом файле, то используем выражение
# if __name__ == '__main__':
# и помещаем ненужный нам код внутрь

# хороший код выглядит так: для простого исполняемого кода
# пишем блок if __name__ == '__main__':
# а любые объявления функций выносим вне его
import calc


def factorial(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


def get_handle():
    handle = input('Enter Twitter username: ')
    return handle


if __name__ == '__main__':
    h = get_handle()
    lenght = len(h)
    print('Username has', lenght, 'characters')

if __name__ == '__main__':
    def example(x):
        return x + 1


    print(example(5))

if __name__ == '__main__':
    a = calc.my_sum(1, 6)
    print(a)
    # модуль берет имя файла потому что мы его импортируем

    print(example(10))
