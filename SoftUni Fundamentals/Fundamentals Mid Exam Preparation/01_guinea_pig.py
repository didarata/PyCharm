quantity_food_kg = float(input()) * 1000
quantity__hay_kg = float(input()) * 1000
quantity_cover_kg = float(input()) * 1000
pig_weight_kg = float(input()) * 1000


for day in range(1, 30 + 1):
    quantity_food_kg -= 300
    if day % 2 == 0:
        quantity__hay_kg -= quantity_food_kg * 0.05
    if day % 3 == 0:
        quantity_cover_kg -= pig_weight_kg / 3
    if quantity_food_kg < 0 or quantity__hay_kg < 0 or quantity_cover_kg < 0:
        print(f'Merry must go to the pet store!')
        exit()

quantity_food_kg /= 1000
quantity__hay_kg /= 1000
quantity_cover_kg /= 1000


print(f'Everything is fine! Puppy is happy! Food: {quantity_food_kg:.2f}, Hay: {quantity__hay_kg:.2f}, Cover: {quantity_cover_kg:.2f}.')



# 10
# 5
# 5.2
# 1

# 1
# 1.5
# 3
# 1.5

# 9
# 5
# 5.2
# 1