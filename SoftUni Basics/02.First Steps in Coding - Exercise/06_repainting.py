nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_price = (nylon + 2) * 1.50
paint_price = ((paint * 0.10) + paint) * 14.50
thinner_price = thinner * 5.00
bags = 0.40

total_price = nylon_price + paint_price + thinner_price + bags
workers_price = (total_price * 0.30) * hours
final_price = total_price + workers_price
print(final_price)