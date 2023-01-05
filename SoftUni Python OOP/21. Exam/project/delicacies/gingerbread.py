from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    def __init__(self, name: str, price: float):
        super().__init__(name, 200, price)
        self.delicacy_type = "Gingerbread"

    def details(self):
        return super().details()
        # return f"Gingerbread {self.name}: {self.portion}g - {self.price:.2f}lv."
