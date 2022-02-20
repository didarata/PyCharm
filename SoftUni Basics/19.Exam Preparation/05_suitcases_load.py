trunk_capacity = float(input())
luggage = input()
total_luggage_volume = 0
luggage_counter = 0
extra_volume = 0

while luggage != 'End':
    luggage_volume = float(luggage)
    total_luggage_volume += luggage_volume
    if trunk_capacity > total_luggage_volume:
        luggage = input()
    if trunk_capacity < total_luggage_volume:
        break
    luggage_counter += 1
    if luggage_counter % 3 == 0:
        volume = luggage_volume * 0.10
        total_luggage_volume += volume

if trunk_capacity > total_luggage_volume:
    print('Congratulations! All suitcases are loaded!')
    print(f'Statistic: {luggage_counter} suitcases loaded.')
else:
    print("No more space!")
    print(f'Statistic: {luggage_counter} suitcases loaded.')