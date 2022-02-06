stadium_capacity = int(input())
total_fans = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for i in range(total_fans):
    fan_in_sector = input()
    if fan_in_sector == 'A':
        sector_a += 1
    elif fan_in_sector == 'B':
        sector_b += 1
    elif fan_in_sector == 'V':
        sector_v += 1
    elif fan_in_sector == 'G':
        sector_g += 1

sector_a_percentage = (sector_a / total_fans) * 100
sector_b_percentage = (sector_b / total_fans) * 100
sector_v_percentage = (sector_v / total_fans) * 100
sector_g_percentage = (sector_g / total_fans) * 100
all_fans = (total_fans / stadium_capacity) * 100

print(f'{sector_a_percentage:.2f}%')
print(f'{sector_b_percentage:.2f}%')
print(f'{sector_v_percentage:.2f}%')
print(f'{sector_g_percentage:.2f}%')
print(f'{all_fans:.2f}%')