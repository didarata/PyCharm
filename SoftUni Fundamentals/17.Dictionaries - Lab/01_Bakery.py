food_list = input().split(' ')
bakery = {}
for item in range(0, len(food_list), 2):
    key = food_list[item]
    value = food_list[item + 1]
    bakery[key] = int(value)
print(bakery)
