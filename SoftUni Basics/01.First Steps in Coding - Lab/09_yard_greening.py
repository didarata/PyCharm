square_meters = float(input())
price_per_square_meter = 7.61
price = square_meters * price_per_square_meter
discount = price * 0.18
final_price = price - discount

print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv')