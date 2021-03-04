while True:
    try:
        a = int(input('Input number 1: '))
        b = (input('Input operation: '))
        c = int(input('Input number 2: '))
    except ValueError:
        print('enter only numbers, please')
    except ZeroDivisionError:
        print('Division by zero is forbidden!')


    def summ():
        if b == '+':
            return a + c
        print(summ())


    def subtr():
        if b == '-':
            return a - c
        print(subtr())


    def mult():
        if b == '*':
            return a * c
        print(mult())


    def div():
        if b == '/':
            return a / c
        print(div())


    def exp():
        if b == '**':
            return a ** c
        print(exp())


    def sqrt():
        if b == 'sqrt':
            return a ** (0.5)
        print(sqrt())


    if b == '+':
        print(summ())
    elif b == '-':
        print(subtr())
    elif b == '*':
        print(mult())
    elif b == '/':
        print(div())
    elif b == '**':
        print(exp())
    elif b == 'sqrt':
        print(sqrt())
    else:
        print('enter valid operation command, '
              'choose from +, -, *, /, **, sqrt')
