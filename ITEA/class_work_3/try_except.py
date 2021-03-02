try:
    n1 = int(input('enter number: '))
    n2 = int(input('enter number: '))
except ValueError:
    print('enter only numbers!')
    exit()
else:
    print(n1 / n2)
    print('cool numbers!')

finally:
    print('finally code block')

# try:
#     print(n1 / n2)
# except ZeroDivisionError:
#     print('danger zone')
#dont do it zone
# try:
#     'some code'
# except:
#     pass

#EP8: E722 do not use bare 'except'
