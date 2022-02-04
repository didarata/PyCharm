from math import pi

figure = input()
side_a = float(input())
result=0
if figure == 'square':
    result = side_a * side_a
elif figure == 'rectangle':
    side_b = float(input())
    result = side_a * side_b
elif figure == 'circle':
    result = pi * side_a * side_a
elif figure == 'triangle':
    side_b = float(input())
    result = side_a * side_b / 2

print(f'{result:.3f}')