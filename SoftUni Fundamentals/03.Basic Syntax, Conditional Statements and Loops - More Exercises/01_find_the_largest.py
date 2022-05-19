num = input()
largest_number = []

for numbers in num:
    largest_number.append(numbers)
    largest_number.sort(reverse=True)
for digit in largest_number:
    print(digit, end='')