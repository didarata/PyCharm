orders = int(input())
price_for_coffee = 0
total = 0

for i in range(1, orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if 0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsules_needed_per_day <= 2000:
        price_for_coffee = capsules_needed_per_day * days * price_per_capsule
        total += price_for_coffee
        print(f'The price for the coffee is: ${price_for_coffee:.2f}')
print(f'Total: ${total:.2f}')
