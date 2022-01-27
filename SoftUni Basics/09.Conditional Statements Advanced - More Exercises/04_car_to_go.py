budged = float(input())
season = input()

car_class = ''
car = ''
price = 0

if budged <= 100:
    car_class = 'Economy class'
    if season == 'Summer':
        car = 'Cabrio'
        price = budged * 0.35
    if season == 'Winter':
        car = 'Jeep'
        price = budged * 0.65

if 100 < budged <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        car = 'Cabrio'
        price = budged * 0.45
    if season == 'Winter':
        car = 'Jeep'
        price = budged * 0.80

if budged > 500:
    car_class = 'Luxury class'
    car = 'Jeep'
    price = budged * 0.90

print(car_class)
print(f'{car} - {price:.2f}')