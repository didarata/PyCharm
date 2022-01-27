count_hrizantemi = int(input())
count_roses = int(input())
count_laleta = int(input())
season = input()
is_holiday = input()

hrizantemi = 0
roses = 0
laleta = 0
total_price = 0

if season in 'Spring Summer':
    hrizantemi = count_hrizantemi * 2
    roses = count_roses * 4.10
    laleta = count_laleta * 2.50
elif season in 'Autumn Winter':
    hrizantemi = count_hrizantemi * 3.75
    roses = count_roses * 4.50
    laleta = count_laleta * 4.15

total_price = hrizantemi + roses + laleta

if is_holiday == 'Y':
    total_price += total_price * 0.15
elif is_holiday == 'N':
    total_price = total_price

if season == 'Spring' and count_laleta > 7:
    total_price -= total_price * 0.05
elif season == 'Winter' and count_roses >= 10:
    total_price -= total_price * 0.10

if season in 'Spring Summer Autumn Winter' and (count_laleta + count_roses + count_hrizantemi) > 20:
    total_price -= total_price * 0.20

total = total_price + 2

print(f'{total:.2f}')