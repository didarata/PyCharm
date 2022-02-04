import sys

number = int(input())

total_sum = 0
max = -sys.maxsize

for i in range(number):
    value = int(input())
    total_sum += value
    if value > max:
        max = value

total_sum -= max
diff = abs(total_sum - max)

if total_sum == max:
    print('Yes')
    print(f'Sum = {max}')
else:
    print('No')
    print(f'Diff = {diff}')