def bang():
    print('I am a function')

a = [1, 2, 3]
a.append(4)
a.append(bang)#добавляем объект функции в список
print(a)
a[4]()#вызываем саму функцию из списка через ()
