try:
    n1 = int(input('enter number: '))
    n2 = int(input('enter number: '))
except (ValueError, KeyError):
    print('enter only numbers!')
    exit()
except RuntimeError:
    print('this is runtime error')
try:
    print(n1 / n2)
except ZeroDivisionError:
    print('danger zone')

