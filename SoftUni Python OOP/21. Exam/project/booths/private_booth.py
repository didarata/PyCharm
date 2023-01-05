from project.booths.booth import Booth


class PrivateBooth(Booth):
    def __init__(self, booth_number: int,  capacity: int):
        super().__init__(booth_number, capacity)
        self.pricePerPeron = 3.5

    def reserve(self, number_of_people: int):
        super().reserve(number_of_people)
