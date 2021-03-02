n1 = int(input('enter number: '))
n2 = int(input('enter number: '))

try:
    print(n1 / n2)
except ZeroDivisionError:
    print('danger zone')

