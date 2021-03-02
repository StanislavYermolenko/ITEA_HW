number = '' #plug

while not isinstance(number, int):
    try:
        number = int(input('enter a number: '))
    except ValueError:
        print('only numbers please')

print(number + 10)

