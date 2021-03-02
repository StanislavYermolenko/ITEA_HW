try:
    n1 = int(input('enter number: '))
    n2 = int(input('enter number: '))
except ValueError:
    print('enter only numbers!')
    exit(1)#end script without continuing
try:
    print(n1 / n2)
except ZeroDivisionError:
    print('danger zone')

