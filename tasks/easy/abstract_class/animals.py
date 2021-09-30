"""
Описать абстрактный класс Animal у которого:

- атрибут name - кличка (тип str)
- магический метод __init__, который принимает аргумент name
- абстрактный метод says, который не принимает аргументов

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод
says таким образом, чтобы он возвращал строку вида:

- "{кличка} - кошка. Говорит МЯУ!" для класса Cat
- "{кличка} - собака. Говорит ГАВ!" для класса Dog
- "{кличка} - корова. Говорит МУ!" для класса Cow
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    name: str

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def says(self):
        raise NotImplementedError


class Cat(Animal):
    def says(self):
        return f'{self.name} - кошка. Говорит МЯУ!'


class Dog(Animal):
    def says(self):
        return f'{self.name} - собакен. Говорит ГАВ!'


class Cow(Animal):
    def says(self):
        return f'{self.name} - корова. Говорит МУ!'


s = Cat("Miavkala")
d = Dog("Gavkala")
c = Cow("Mukala")
print(s.says())
print(d.says())
print(c.says())

