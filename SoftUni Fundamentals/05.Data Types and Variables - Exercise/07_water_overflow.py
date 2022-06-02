number_of_lines = int(input())

tank_capacity = 255
current_capacity = 0

for _ in range(number_of_lines):
    litters_of_water = int(input())
    current_capacity += litters_of_water
    if tank_capacity < current_capacity:
        print('Insufficient capacity!')
        current_capacity -= litters_of_water
    else:
        continue
print(current_capacity)
