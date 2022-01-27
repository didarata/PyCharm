chicken_menu = int(input())
fish_menu = int(input())
vegi_menu = int(input())

chicken_menu_price = chicken_menu * 10.35
fish_menu_price = fish_menu * 12.40
vegi_menu_price = vegi_menu * 8.15
total_price = chicken_menu_price + fish_menu_price + vegi_menu_price
desert = total_price * 0.20
delivery = 2.50

final_price = total_price + desert + delivery

print(final_price)