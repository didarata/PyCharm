from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    def __init__(self, name: str, price: float):
        super().__init__(name, 250, price)
        self.delicacy_type = "Stolen"

    def details(self):
        return super().details()
        # return f"Stolen {self.name}: {self.portion}g - {self.price:.2f}lv."
