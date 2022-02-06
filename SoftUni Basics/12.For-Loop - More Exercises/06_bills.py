months = int(input())

electricity = 0
water = 0
internet = 0
other = 0

for i in range(months):
    electricity_per_month = float(input())
    electricity += electricity_per_month
    electricity1 = electricity_per_month
    water += 20
    internet += 15
    other += (electricity1 + 20 + 15) + ((electricity1 + 20 + 15) * 0.20)


average = (electricity + water + internet + other) / months

print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average:.2f} lv')