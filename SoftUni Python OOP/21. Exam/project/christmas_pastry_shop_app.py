from project.delicacies.stolen import Stolen
from project.delicacies.gingerbread import Gingerbread
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in [ele.name for ele in self.delicacies]:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in ["Stolen", "Gingerbread"]:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        if type_delicacy == "Stolen":
            self.delicacies.append(Stolen(name, price))
        elif type_delicacy == "Gingerbread":
            self.delicacies.append(Gingerbread(name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in [ele.booth_number for ele in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in ["Open Booth", "Private Booth"]:
            raise Exception(f"{type_booth} is not a valid booth!")
        if type_booth == "Open Booth":
            self.booths.append(
                OpenBooth(booth_number, capacity))
        elif type_booth == "Private Booth":
            self.booths.append(
                PrivateBooth(booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if booth.capacity >= number_of_people and not booth.is_reserved:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        boothNumbers = [ele.booth_number for ele in self.booths]
        if booth_number not in boothNumbers:
            raise Exception(f"Could not find booth {booth_number}!")
        if delicacy_name not in [ele.name for ele in self.delicacies]:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        for booth in self.booths:
            if booth_number == booth.booth_number:
                for delicacy in self.delicacies:
                    if delicacy.name == delicacy_name:
                        booth.delicacy_orders.append(delicacy)
                        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
            for i in range(len(self.booths)):
                if self.booths[i].booth_number == booth_number:
                    da = i
                    break
            priceToPay = self.booths[da].price_for_reservation + sum([deli.price for deli in self.booths[da].delicacy_orders])
            self.booths[da].price_for_reservation = 0
            self.booths[da].delicacy_orders = []
            self.booths[da].is_reserved = False
            self.income += priceToPay
            return f"Booth {booth_number}:\nBill: {priceToPay:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."


# shop = ChristmasPastryShopApp()
# print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
# print(shop.delicacies[0].details())
# print(shop.add_booth("Open Booth", 1, 30))
# print(shop.add_booth("Private Booth", 10, 5))
# print(shop.reserve_booth(30))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.reserve_booth(5))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.get_income())
