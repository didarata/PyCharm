class Chef:

    def make_chicken(self):
        print("The chef makes a chicken!")

    def make_salad(self):
        print("The chef makes a salad!")

    def make_special_dish(self):
        print("The chef makes bbq ribs!")

class ChineseChef(Chef):

    def make_fried_rice(self):
        print("The chef makes fried rice!")

    def make_special_dish(self):
        print("The chef makes orange chiken!")


myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()