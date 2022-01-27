vegi_price = float(input())
fruit_price = float(input())
vegi_kg = int(input())
fruit_kg = int(input())

vegi_total = vegi_kg * vegi_price
fruit_total = fruit_kg * fruit_price
total_euro = (vegi_total + fruit_total) / 1.94
print(f'{total_euro:.2f}')