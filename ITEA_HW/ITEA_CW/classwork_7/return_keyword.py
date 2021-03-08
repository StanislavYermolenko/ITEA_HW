#пример с калькулятором
def my_sum(a, b):
    return a + b

def my_sub(a, b):
    return a - b

def my_mul(a, b):
    return a * b

def my_div(a, b):
    return a / b

OPERATORS = {
    '+': my_sum,
    '-': my_sum,
    '*': my_mul,
    '/': my_div

}

number1 = int(input('enter number 1: '))
operator = input('input operator: ')
number2 = int(input('enter number 2: '))
#если оператор находится среди ключей словаря OPERATOR, по ключу operator
if operator in OPERATORS:#берем значение - нужную нам функцию и вызываем ее
    print('result:', OPERATORS[operator](number1, number2))
else:#передавая нужные нам значения - number1, number2
    print('operator not supported')

