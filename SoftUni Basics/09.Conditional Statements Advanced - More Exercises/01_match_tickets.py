budget = float(input())
category_ticket = input()
people_in_the_group = int(input())

vip_ticket = 499.99
normal_ticket = 249.99
transport = 0
cost = 0
diff = 0

if 1 <= people_in_the_group <= 4:
    transport = budget * 0.75
elif people_in_the_group <= 9:
    transport = budget * 0.60
elif people_in_the_group <= 24:
    transport = budget * 0.50
elif people_in_the_group <= 49:
    transport = budget * 0.40
elif people_in_the_group > 50:
    transport = budget * 0.25

if category_ticket == 'VIP':
    cost = vip_ticket * people_in_the_group
elif category_ticket == 'Normal':
    cost = normal_ticket * people_in_the_group

diff = abs(budget - cost - transport)

if budget >= (cost + transport):
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')