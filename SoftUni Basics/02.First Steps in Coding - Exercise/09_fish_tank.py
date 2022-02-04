lenght = int(input())
width = int(input())
height = int(input())
percent_taken_by_other = float(input()) / 100

tank_volume = lenght * width * height
volume_liters = tank_volume / 1000
water_needed = volume_liters - (volume_liters * percent_taken_by_other)

print(water_needed)