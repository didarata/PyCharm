film_budged = float(input())
cast = int(input())
cast_cloths = float(input())

decor = film_budged * 0.10
total_cast_cloths = cast * cast_cloths

if cast > 150:
    total_cast_cloths -= total_cast_cloths * 0.10

total_film_price = decor + total_cast_cloths
money_left = abs(total_film_price - film_budged)

if film_budged >= total_film_price:
   print(f'Action!')
   print(f'Wingard starts filming with {money_left:.2f} leva left.')
else:
    print(f'Not enough money!')
    print(f'Wingard needs {money_left:.2f} leva more.')