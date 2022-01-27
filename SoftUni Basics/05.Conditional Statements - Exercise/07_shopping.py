budget = float(input())
video_card = int(input())
cpu = int(input())
ram = int(input())

video_card_price = video_card * 250
cpu_price = (video_card_price * 0.35) * cpu
ram = (video_card_price * 0.10) * ram
total_price = video_card_price + cpu_price + ram

if video_card > cpu:
    total_price -= total_price * 0.15

diff = abs(budget - total_price)

if budget >= total_price:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')