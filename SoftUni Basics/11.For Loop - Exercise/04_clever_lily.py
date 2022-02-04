lilly_age = int(input())
washing_machine_price = float(input())
price_per_toy = float(input())

toys = 0
birthday_money = 0

for birthday in range(1, lilly_age + 1):
    if birthday % 2 == 0:
        birthday_money += birthday * 5 - 1
    else:
        toys += 1

total_toys = toys * price_per_toy
total_savings = total_toys + birthday_money
diff = abs(total_savings - washing_machine_price)

if total_savings >= washing_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')