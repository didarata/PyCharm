lines = int(input())
sum_of_numbers = 0
for i in range(lines):
    lines = input()
    sum_of_numbers += ord(lines)

print(f'The sum equals: {sum_of_numbers}')
