number = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, number + 1):
    value = int(input())
    if value < 200:
        p1 += 1
    elif 200 <= value <= 399:
        p2 += 1
    elif 400 <= value <= 599:
        p3 += 1
    elif 600 <= value <= 799:
        p4 += 1
    elif value >= 800:
        p5 += 1

print(f'{p1 / number * 100:.2f}%')
print(f'{p2 / number * 100:.2f}%')
print(f'{p3 / number * 100:.2f}%')
print(f'{p4 / number * 100:.2f}%')
print(f'{p5 / number * 100:.2f}%')