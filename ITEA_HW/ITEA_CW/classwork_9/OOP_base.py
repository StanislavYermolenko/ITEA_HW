# класс - схема для конструкции объекта
# # у классов есть методы, по сути это функции
# # созданные внутри класса
# class Car:
#     manufacturer = 'Mitsubishi'
# # self - представитель класса к которому вызывается метод
# a = Car()  # создаем объект класса
# a.ride()  # применяем к нему метод upper_name()
# def ride(self):
#     print('vroom vroom from {}'.format(self.manufacturer))

# конструктор класса - специальный метод внутри класса
# который позволяет сконструировать представителя класса
# и передеть ему какие-то параметры, также конструктор позволяет
# конфигурировать и параметризировать создание представителей класса
# а методы по сути это описание поведения наших представителей.
# self внутри этого описания это указатель на сам представитель
# из которого этот метод будет вызван
class Cat:

    def __init__(self, name):
        self.name = name

    def say(self):
        return 'my name is {}'.format(self.name)

    def rename(self, new_name):
        self.name = new_name


bingo = Cat(name="Bingo")
marta = Cat(name='Marta')
print(marta.say())
marta.rename('Agata')
print(bingo.say())
print(marta.say())
# изменение параматра также возможно
marta.name = 'Kisa'
# узнать все методы объекта print(dir(bingo))
print(marta.say())
# хорошая практика когда все параметры с которыми
# работает представитель класса описаны в конструкторе!
