import math

days = int(input())
food_for_pets_kg = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_kg = float(input())

food_dog_needs = days * dog_food_per_day_kg
food_cat_needs = days * cat_food_per_day_kg
food_turtle_needs = (days * turtle_food_per_day_kg) / 1000
total_food = food_dog_needs + food_cat_needs + food_turtle_needs
food_left = abs(food_for_pets_kg - total_food)

if total_food <= food_for_pets_kg:
    print(f'{math.floor(food_left)} kilos of food left.')
else:
    print(f'{math.ceil(food_left)} more kilos of food are needed.')