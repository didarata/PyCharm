command = input().split("||")

targeted_cities = {}


while command[0] != "Sail":
    city, population, gold = command
    population = int(population)
    gold = int(gold)
    if command[0] not in targeted_cities:
        targeted_cities[city] = {"population": population, "gold": gold}
    else:
        targeted_cities[city]["population"] += population
        targeted_cities[city]["gold"] += gold

    command = input().split("||")

command = input().split("=>")

while command[0] != "End":

    if command[0] == "Plunder":
        command, city, population, gold = command
        population = int(population)
        gold = int(gold)

        targeted_cities[city]["population"] -= population
        targeted_cities[city]["gold"] -= gold
        print(f'{city} plundered! {gold} gold stolen, {population} citizens killed.')
        if targeted_cities[city]["population"] <= 0 or targeted_cities[city]["gold"] <= 0:
            print(f'{city} has been wiped off the map!')
            del targeted_cities[city]

    if command[0] == "Prosper":
        command, city, gold = command
        gold = int(gold)
        if gold <= 0:
            print('Gold added cannot be a negative number!')
        else:
            targeted_cities[city]["gold"] += gold
            print(f'{gold} gold added to the city treasury. {city} now has {targeted_cities[city]["gold"]} gold.')

    command = input().split("=>")

if len(targeted_cities) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f'Ahoy, Captain! There are {len(targeted_cities.keys())} wealthy settlements to go to:')
    for cities in targeted_cities:
        print(f'{cities} -> Population: {targeted_cities[cities]["population"]} citizens, Gold: {targeted_cities[cities]["gold"]} kg')
