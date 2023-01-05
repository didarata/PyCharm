import delicacies.delicacy as dl


class Gingerbread(dl.Delicacy):
    def __init__(self, name: str, price: float):
        super().__init__(name, 200, price)

    def details(self):
        return f"Gingerbread {self.name}: {self.portion}g - {self.price:.2f}lv."
