import math

count_balls = int(input())

total_points = 0
count_red = 0
count_orange = 0
count_yellow = 0
count_white = 0
count_black = 0
count_other = 0

for ball in range(1, count_balls + 1):
    color = input()
    if color == 'red':
        total_points += 5
        count_red += 1
    elif color == 'orange':
        total_points += 10
        count_orange += 1
    elif color == 'yellow':
        total_points += 15
        count_yellow += 1
    elif color == 'white':
        total_points += 20
        count_white += 1
    elif color == 'black':
        total_points /= 2
        count_black += 1
    else:
        count_other += 1


print(f'Total points: {math.floor(total_points)}')
print(f'Points from red balls {count_red}')
print(f"Points from orange balls {count_orange}")
print(f"Points from yellow balls {count_yellow}")
print(f"Points from white balls {count_white}")
print(f"Other colors picked: {count_other}")
print(f'Divides from black balls: {count_black}')