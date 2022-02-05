count_loads = int(input())

van = 0
truck = 0
train = 0
total_tons = 0

for i in range(count_loads):
    tons_loads = float(input())
    if tons_loads <= 3:
        van += tons_loads
        total_tons += tons_loads
    elif tons_loads <= 11:
        truck += tons_loads
        total_tons += tons_loads
    else:
        train += tons_loads
        total_tons += tons_loads

van_price = van * 200
truck_price = truck * 175
train_price = train * 120
average_price_per_ton = (van_price + truck_price + train_price) / total_tons
van_procentage = (van / total_tons) * 100
truck_procentage = (truck / total_tons) * 100
train_procentage = (train / total_tons) * 100


print(f'{average_price_per_ton:.2f}')
print(f'{van_procentage:.2f}%')
print(f'{truck_procentage:.2f}%')
print(f'{train_procentage:.2f}%')