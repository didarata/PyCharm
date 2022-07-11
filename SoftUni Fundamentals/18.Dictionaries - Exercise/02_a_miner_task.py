resources = {}
while True:
    current_resource = input()
    if current_resource == "stop":
        break
    quantity = int(input())
    if current_resource not in resources.keys():
        resources[current_resource] = 0
    resources[current_resource] += quantity
for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")


# gold
# 155
# silver
# 10
# copper
# 17
# gold
# 15
# stop

# Gold
# 155
# Silver
# 10
# Copper
# 17
# stop