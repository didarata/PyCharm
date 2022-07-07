class Inventory:
    def __init__(self, __capacity: int):
        self.capacity = __capacity
        self.capacity_left = __capacity
        self.items = []

    def add_item(self, item: str):
        if self.capacity_left > 0:
            self.items.append(item)
            self.capacity_left -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.capacity_left}"

