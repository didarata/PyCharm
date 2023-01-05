import booths.booth as bo


class PrivateBooth (bo.Booth):
    def __init__(self, booth_number: int,  capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        super().reserve(number_of_people=number_of_people)
