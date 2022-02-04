money = float(input())
year = int(input())

even_year = 0
odd_year = 0
ivan_years = 17

for i in range(1800, year + 1):
    ivan_years += 1
    if i % 2 == 0:
        even_year += 12000
    else:
        odd_year += 12000 + ivan_years * 50

total_money_spend = odd_year + even_year
money_left = abs(money - total_money_spend)

if money >= total_money_spend:
    print(f'Yes! He will live a carefree life and will have {money_left:.2f} dollars left.')
else:
    print(f'He will need {money_left:.2f} dollars to survive.')