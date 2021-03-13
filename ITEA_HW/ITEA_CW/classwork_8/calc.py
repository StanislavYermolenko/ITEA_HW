def my_sum(a, b):
    return a + b


if __name__ == '__main__':

    while True:
        try:
            a = int(input('Input number 1: '))
            b = int(input('Input number 2: '))
        except ValueError:
            print('enter only numbers, please')

        print(my_sum(a, b))
