season = input()
type_of_group = input()
count_students = int(input())
count_nights = int(input())

boys = 0
girls = 0
mixed = 0
price = 0
sport = ''

if season == 'Winter':
    boys = 9.60 * count_students * count_nights
    girls = 9.60 * count_students * count_nights
    mixed = 10 * count_students * count_nights
elif season == 'Spring':
    boys = 7.20 * count_students * count_nights
    girls = 7.20 * count_students * count_nights
    mixed = 9.50 * count_students * count_nights
elif season == 'Summer':
    boys = 15 * count_students * count_nights
    girls = 15 * count_students * count_nights
    mixed = 20 * count_students * count_nights

if type_of_group == 'boys':
    price = boys
elif type_of_group == 'girls':
    price = girls
elif type_of_group == 'mixed':
    price = mixed

if count_students >= 50:
    price -= price * 0.50
elif count_students >= 20:
    price -= price * 0.15
elif count_students >= 10:
    price -= price * 0.05

if type_of_group == 'girls' and season == 'Winter':
    sport = 'Gymnastics'
elif type_of_group == 'girls' and season == 'Spring':
    sport = 'Athletics'
elif type_of_group == 'girls' and season == 'Summer':
    sport = 'Athletics'
elif type_of_group == 'boys' and season == 'Winter':
    sport = 'Judo'
elif type_of_group == 'boys' and season == 'Spring':
    sport = 'Tennis'
elif type_of_group == 'boys' and season == 'Summer':
    sport = 'Football'
elif type_of_group == 'mixed' and season == 'Winter':
    sport = 'Ski'
elif type_of_group == 'mixed' and season == 'Spring':
    sport = 'Cycling'
elif type_of_group == 'mixed' and season == 'Summer':
    sport = 'Swimming'

print(f'{sport} {price:.2f} lv.')