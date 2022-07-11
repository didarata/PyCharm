import itertools

inventory = {}
products = input().split(" ")

while products[0] != "buy":
    name, price, quantity = products
    if name not in inventory.keys():
        inventory[name] = price, quantity
    else:
        for name, value in inventory.items():
            if name == products[0]:
                price_change, quantity_change = itertools.islice(value, 2)
                inventory[name] = price, (int(quantity) + int(quantity_change))
    products = input().split(" ")

for name, result in inventory.items():
    print(f"{name} -> {float(result[0]) * float(result[1]):.2f}")




# Beer 2.20 100
# IceTea 1.50 50
# NukaCola 3.30 80
# Water 1.00 500
# buy


# Beer 2.40 350
# Water 1.25 200
# IceTea 5.20 100
# Beer 1.20 200
# IceTea 0.50 120
# buy

# CesarSalad 10.20 25
# SuperEnergy 0.80 400
# Beer 1.35 350
# IceCream 1.50 25
# buy