import math

count_paint = int(input())
count_wallpaper = int(input())
price_gloves = float(input())
price_brush = float(input())

paint = 21.50
wallpaper = 5.20
count_gloves = math.ceil(count_wallpaper * 0.35)
count_brushes = math.floor(count_paint * 0.48)

total_paint_price = count_paint * paint
total_wallpaper_price = count_wallpaper * wallpaper
total_gloves_price = count_gloves * price_gloves
total_brushes_price = count_brushes * price_brush

total_price = total_gloves_price + total_brushes_price + total_paint_price + total_wallpaper_price
delivery_cost = total_price / 15

print(f'This delivery will cost {delivery_cost:.2f} lv.')