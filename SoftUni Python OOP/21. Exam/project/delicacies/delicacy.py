from abc import ABC, abstractmethod


class Delicacy(ABC):
    def __init__(self, name: str, portion: int, price: float):
        self.name = name
        self.portion = portion
        self.price = price
        self.delicacy_type = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == "" or name.replace(" ", "") == "":
            raise ValueError("Name cannot be null or whitespace!")
        self.__name = name

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, portion):
        self.__portion = portion

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError("Name cannot be null or whitespace!")
        self.__price = price

    @abstractmethod
    def details(self):
        return f"{self.delicacy_type} {self.name}: {self.portion}g - {self.price:.2f}lv."
