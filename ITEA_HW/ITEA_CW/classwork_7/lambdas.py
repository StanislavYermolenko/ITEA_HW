#функции без имени lambda a, b: a + b
#должна состоять из одного выражения
#запрещено присваивание!, генерируют объект
#функции без имени, пример калькулятора,
#нельзя обработать исключения!

OPERATORS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '**': lambda a, b: a ** b,
}

number1 = int(input('enter number 1: '))
operator = input('input operator: ')
number2 = int(input('enter number 2: '))


