import math

magnolias_order = int(input())
hyacinths_order = int(input())
roses_order = int(input())
cacti_order = int(input())
gift_price = float(input())

magnolias_price = 3.25 * magnolias_order
hyacinths_price = 4 * hyacinths_order
roses_price = 3.5 * roses_order
cacti_price = 8 * cacti_order
total_price = magnolias_price + hyacinths_price + roses_price + cacti_price
total_price -= total_price * 0.05
diff = abs(gift_price - total_price)

if gift_price <= total_price:
    print(f'She is left with {math.floor(diff)} leva.')
else:
    print(f'She will have to borrow {math.ceil(diff)} leva.')


