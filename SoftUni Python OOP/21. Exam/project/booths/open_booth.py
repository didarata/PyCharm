from project.booths.booth import Booth


class OpenBooth(Booth):
    def __init__(self, booth_number: int, capacity):
        super().__init__(booth_number, capacity)
        self.pricePerPeron = 2.5

    def reserve(self, number_of_people: int):
        super().reserve(number_of_people)
