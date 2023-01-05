from abc import ABC, abstractmethod


class Booth(ABC):

    def __init__(self, booth_number: int, capacity):

        self.booth_number = booth_number
        self.capacity = capacity

        self.price_for_reservation = 0.0
        self.delicacy_orders = []
        self.is_reserved = False
        self.pricePerPeron = 0

    @property
    def booth_number(self):
        return self.__booth_number

    @booth_number.setter
    def booth_number(self, number):
        self.__booth_number = number

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError(f"Capacity cannot be a negative number!")
        self.__capacity = value

    @abstractmethod
    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.price_for_reservation = self.pricePerPeron * number_of_people
