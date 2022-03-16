sweets_type = input()
number_sweets = int(input())
day_from_december = int(input())

if day_from_december <= 15:
    if sweets_type == "Cake":
        price = 24 * number_sweets
    elif sweets_type == "Souffle":
        price = 6.66 * number_sweets
    elif sweets_type == "Baklava":
        price = 12.60 * number_sweets
    price = price - (price * 0.10)
    if 100 <= price < 200:
        price = price - (price * 0.15)
    elif price >= 200:
        price = price - (price * 0.25)

elif day_from_december > 15:
    if sweets_type == "Cake":
        price = 28.70 * number_sweets
    elif sweets_type == "Souffle":
        price = 9.80 * number_sweets
    elif sweets_type == "Baklava":
        price = 16.98 * number_sweets
        if 100 <= price < 200:
            price = price - (price * 0.15)
        elif price >= 200:
            price = price - (price * 0.25)

print(f'{price:.2f}')