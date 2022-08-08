from collections import Counter

command = input().split(':')
area_list = {}

animals= {}

while command[0] != "EndDay":

    if command[0] == "Add":
        animal, food, area = command[1].split("-")
        if animal not in animals:
            animals[animal] = {"food": int(food), "area": area}
        else:
            animals[animal]['food'] += int(food)

    elif command[0] == "Feed":
        animal, food = command[1].split("-")
        if animal in animals:
            animals[animal]["food"] -= int(food)
            if animals[animal]['food'] <= 0:
                print(f'{animal} was successfully fed')
                del animals[animal]


    command = input().split(':')

print("Animals:")
for animal in animals:
    print(f"{animal} -> {animals[animal]['food']}g")
print("Areas with hungry animals:")

for animal in animals:
    animal_area = animals[animal]["area"]
    if animal_area not in area_list:
        area_list[animal_area] = {"count": int(1)}
    else:
        area_list[animal_area]["count"] += 1

for area in area_list:
    print(f'{area}: {area_list[area]["count"]}')