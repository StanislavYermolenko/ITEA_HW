class Example:

    def test(self):  # публичный метод public
        self._test2()
        self.__test3()
        return 'Print test'

    # внутри класса все медоты абсолютно доступны
    def _test2(self):  # защищенный метод _ protected
        return 'test2'

    def __test3(self):  # приватный метод __ private
        return 'test3'


# однако если обратится из представителя, a.__test3()
# то получим ошибку, можем обратиться к нему, только написав
# метод класса a._Encap__test3() все методы будут переданы
# наследнику и к ним можно достучаться
class Weather:

    __CONVERT_MAP = {
        'CF': lambda temp: temp * 1.8 + 32,
        'CK': lambda temp: temp + 273.15,
        'FC': lambda temp: (temp - 32) / 1.8,
        'FK': lambda temp: (temp + 459.67) * (5 / 9),
        'KC': lambda temp: temp - 273.15,
        'KF': lambda temp: temp / (5 / 9) - 459.67,
    }

    def __init__(self, temp, format='C'):
        self.temp = temp
        self.format = format

    def get_celcius(self):
        return "{} C".format(self._convert_value('C'))

    def get_fahrenheit(self):
        return "{} F".format(self._convert_value('F'))

    def get_kelvin(self):
        return "{} K".format(self._convert_value('K'))

    def _convert_value(self, to_):
        if self.format == to_:
            return self.temp
        else:
            return self.__CONVERT_MAP[
                "{}{}".format(self.format, to_)
            ](self.temp)


a = Weather(100, 'C')
print(a.get_celcius())
print(a.get_fahrenheit())

