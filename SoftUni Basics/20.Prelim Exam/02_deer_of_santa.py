import math
count_days_santa_is_gone = int(input())
food_left_kg = float(input())
first_deer_food_per_day = float(input())
second_deer_food_per_day = float(input())
third_deer_food_per_day = float(input())

first_deer = count_days_santa_is_gone * first_deer_food_per_day
second_deer = count_days_santa_is_gone * second_deer_food_per_day
third_deer = count_days_santa_is_gone * third_deer_food_per_day
total_food_needed = first_deer + second_deer + third_deer
food_left = abs(food_left_kg - total_food_needed)

if total_food_needed <= food_left_kg:
    print(f'{math.floor(food_left)} kilos of food left.')
else:
    print(f'{math.ceil(food_left)} more kilos of food are needed.')