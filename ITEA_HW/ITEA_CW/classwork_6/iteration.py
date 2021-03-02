# for i in [0, 1, 2, 3, '344', 4, 5, 'fun', 6, 7, 8, 9]:
#     print('hello ' + str(i))
#главное отличие for from while то что for перебирает
#строку, а while выполняет условие пока не выполнит
#a = 'something interesting' or
a = input('input something: ')#если нужно ограничить до определенного
for i in a: #елемента в списке, ставим for i in a[:5]:
    print(i, end='') #end='' - переход на новую строку
#for i in reversed(a[:5]): #перебор до 5го с конца



