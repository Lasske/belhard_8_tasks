"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""
from datetime import date

CURRENT_YEAR = date.today().year


class BookCard:
    __author: str
    __title: str
    __year: int

    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year

    def __eq__(self, other):
        return self.__year == other.year

    def __lt__(self, other):
        return self.__year < other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if isinstance(value, str):
            self.__author = value
        else:
            raise ValueError

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self.__title = value
        else:
            raise ValueError

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if isinstance(value, int) and 0 < value <= CURRENT_YEAR:
            self.__year = value
        else:
            raise ValueError