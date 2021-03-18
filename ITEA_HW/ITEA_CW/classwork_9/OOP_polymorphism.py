# полиморфизм предполагает что классы и представители классов,
# которые используются в одном и том же участке логики должны
# иметь одинаковый интерфейс работы с ними

# методы которые делают одно и то же называем одинаково
# у разных класов чтобы обеспечить им нормальную работу между собой

class Animal:
    sound = ''

    def say(self):
        print(self.sound)

    def __init__(self, name, height=1):
        self.name = name
        self.height = height

    def jump(self):
        print('I jump {} meters'.format(self.height * 1.5))


class Cat(Animal):
    sound = 'MEOW'


class Dog(Animal):
    sound = 'WOOF'


class Stork:
    sound = 'Click-click-click-click!'

    def __init__(self, name, height=2):
        self.name = name
        self.height = height

    def say(self):
        print(self.sound)


def pet_an_animal(animal):
    print("I'm petting an animal")
    animal.say()


a = Cat('Agata')
b = Dog('Barny')
c = Stork('Miles')

pet_an_animal(a)
pet_an_animal(b)
pet_an_animal(c)

# полиморфизм приводит нас к так называемой "утиной типизации"
# при применении какого-либо оператора или функции python
# проверяет не типы а способность объекта на это действие, например '+'

