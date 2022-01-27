house_height = float(input())
lenght_side_wall = float(input())
height_roof = float(input())

side_wall = house_height * lenght_side_wall
window = 1.5 * 1.5
two_side_walls = (side_wall * 2) - (2 * window)
back_side_wall = house_height * house_height
front_side = back_side_wall - (1.2 * 2)
front_and_back = back_side_wall + front_side
total_walls = two_side_walls + front_and_back
green_paint_needed = total_walls / 3.4

roof_front_and_back = 2 * (house_height * lenght_side_wall)
roof_sides = 2 * (house_height * height_roof / 2)
total_roof = roof_front_and_back + roof_sides
red_paint_needed = total_roof / 4.3

print(f'{green_paint_needed:.2f}')
print(f'{red_paint_needed:.2f}')
