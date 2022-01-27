budged = float(input())
season = input()

accommodation = ''
location = ''
price = 0

if budged <= 1000:
    accommodation = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budged * 0.65
    if season == 'Winter':
        location = 'Morocco'
        price = budged * 0.45

if 1000 < budged <= 3000:
    accommodation = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budged * 0.80
    if season == 'Winter':
        location = 'Morocco'
        price = budged * 0.60

if budged > 3000:
    accommodation = 'Hotel'
    if season == 'Summer':
        location = 'Alaska'
        price = budged * 0.90
    if season == 'Winter':
        location = 'Morocco'
        price = budged * 0.90

print(f'{location} - {accommodation} - {price:.2f}')