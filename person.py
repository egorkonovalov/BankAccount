class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        """ The docstring for the age property """
        print('In age method')
        return self._age

    @age.setter
    def age(self, value):
        print('In set_age method(', value, ')')
        if isinstance(value,int) & (value > 0 & value < 120):
            self._age = value
        else:
            raise InvalidAgeException(value)

    @property
    def name(self):
        print('In name')
        return self._name

    @name.deleter
    def name(self):
        del self._name

    def __str__(self):
        return 'Person[' + str(self._name) + '] is ' + self._age

class InvalidAgeException(Exception):
    """ Valid Ages must be between 0 and 120 """

    def __init__(self, value):
        self.value = value

    def __str__(self):
            return 'InvalidAgeException(' + str(self.value) + ')'

try:
    p = Person('Adam', 21)
    p.age = -1

except InvalidAgeException as e:
    print(e)