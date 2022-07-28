command = input().split("||")

targeted_cities = {}


while command[0] != "Sail":
    city, population, gold = command
    if command[0] not in targeted_cities:
        targeted_cities[city] = population, gold
        targeted_cities.update({targeted_cities[city]: "White"})
    else:
        targeted_cities.update("baba", "gaga")

    command = input().split("||")



command = input().split("=>")

while command[0] != "End":
    pass

    command = input().split("=>")

test one two targeted_cities