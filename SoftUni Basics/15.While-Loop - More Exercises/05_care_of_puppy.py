bought_food_kg = int(input())
bought_food_gr = bought_food_kg * 1000

total_eaten_gr = 0
command = input()

while command != "Adopted":
    eaten_gr = int(command)
    total_eaten_gr += eaten_gr
    command = input()
else:
    if bought_food_gr >= total_eaten_gr:
        left_food = bought_food_gr = total_eaten_gr
        print(f'Food is enough! Leftovers: {left_food} grams.')
    else:
        need_food = total_eaten_gr - bought_food_gr
        print(f'Food is not enough. You need {need_food} grams more.')
