while True:
    try:
        y = int(input('input a year: '))
    except ValueError:
        print('its not a number')
        exit(1)
    if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
        print('its not a leap year')
    else:
        print('this is leap year!')
