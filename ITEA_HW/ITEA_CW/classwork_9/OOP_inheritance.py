class Animal:
    sound = ''

    def say(self):
        print(self.sound)

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def jump(self):
        print('I jump {} meters'.format(self.height * 1.5))


class Flying:

    def fly(self):
        print('I am flying')

# множественное наследование
class Cat(Animal, Flying):
    sound = 'MEOW'


class Dog(Animal):
    sound = 'WOOF'


Barney = Dog(name='Barney', height=1)
Barney.say()
Barney.jump()
Barney.say()

Agata = Cat(name='Agata', height=0.5)
Agata.say()
Agata.jump()
Agata.fly()
Agata.say()


# # расширяем наследуемые методы дополнительным функционалом
# # со встроенной функцией super. По сути super() обращается к
# # классу от которого мы наследуемся Animal и вызываем метод jump у него
# class Cat(Animal):
#     sound = 'MEOW'
#
#     def jump(self):
#         super().jump()
#         self.say()
#
#
# # переопределяем метод jump в классе Cat но внутри него
# # вызываем 'оригинальный' метод jump из класса Animal, вызывая потом
# # метод say(). Таким образом мы может отнаследовать метод jump но внутри
# # нашего класса сделать что-то до него или после него







