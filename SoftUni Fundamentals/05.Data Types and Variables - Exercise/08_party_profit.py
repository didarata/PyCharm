import math

group_size = int(input())
days = int(input())

earnings = 0
money_spend = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    earnings += 50
    money_spend += 2 * group_size
    if day % 3 == 0:
        money_spend += 3 * group_size
    if day % 5 == 0:
        earnings += 20 * group_size
        if day % 3 == 0:
            money_spend += 2 * group_size

total_earnings_per_person = (earnings - money_spend) / group_size
print(f'{group_size} companions received {math.floor(total_earnings_per_person)} coins each.')
