budged = float(input())
price_flour = float(input())
price_eggs = price_flour * 0.75
price_milk = price_flour * 1.25
one_loaf_milk = price_milk / 4
price_per_bread = price_eggs + price_flour + one_loaf_milk
bread_range = int(budged / price_per_bread)
breads = 0
colored_eggs = 0
current_price = 0

for i in range(1, bread_range + 1):
    breads += 1
    colored_eggs += 3
    current_price += price_per_bread
    if i % 3 == 0:
        colored_eggs -= (breads - 2)

print(f'You made {breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budged - current_price:.2f}BGN left.')
