fires = input().split('#')
amount_of_water = int(input())
total_fire = 0
print("Cells:")
for index in fires:
    current_fire = index.split(' = ')
    current_type_of_fire = current_fire[0]
    current_range_of_fire = int(current_fire[1])
    if current_type_of_fire == 'Low' and amount_of_water >= current_range_of_fire:
        if 1 <= current_range_of_fire <= 50:
            print(f" - {current_range_of_fire}")
            total_fire += current_range_of_fire
            amount_of_water -= current_range_of_fire
    if current_type_of_fire == 'Medium' and amount_of_water >= current_range_of_fire:
        if 51 <= current_range_of_fire <= 80:
            print(f" - {current_range_of_fire}")
            total_fire += current_range_of_fire
            amount_of_water -= current_range_of_fire
    if current_type_of_fire == "High" and amount_of_water >= current_range_of_fire:
        if 81 <= current_range_of_fire <= 125:
            print(f" - {current_range_of_fire}")
            total_fire += current_range_of_fire
            amount_of_water -= current_range_of_fire

print(f'Effort: {total_fire * 0.25:.2f}')
print(f'Total Fire: {total_fire}')
