import math

square_meter_area = int(input())
grapes_per_square_meter = float(input())
need_liters_wine = int(input())
workers_count = int(input())

total_grapes = square_meter_area * grapes_per_square_meter
total_wine = (total_grapes * 0.40) / 2.5
wine_left = abs(total_wine - need_liters_wine)
liters_per_worker = wine_left / workers_count

if total_wine >= need_liters_wine:
    print(f'Good harvest this year! Total wine: {math.floor(total_wine)} liters.')
    print(f'{math.ceil(wine_left)} liters left -> {math.ceil(liters_per_worker)} liters per person.')
else:
    print(f"It will be a tough winter! More {math.floor(wine_left)} liters wine needed.")