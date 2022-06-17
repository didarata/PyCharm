def positive_number(numbers):
    return [number for number in numbers if int(number) >= 0]


def negative_number(numbers):
    return [number for number in numbers if int(number) < 0]


def even_number(numbers):
    return [number for number in numbers if int(number) % 2 == 0]


def odd_number(numbers):
    return [number for number in numbers if int(number) % 2 != 0]


numbers_as_string = input().split(", ")
print(f'Positive: {", ".join(positive_number(numbers_as_string))}')
print(f'Negative: {", ".join(negative_number(numbers_as_string))}')
print(f'Even: {", ".join(even_number(numbers_as_string))}')
print(f'Odd: {", ".join(odd_number(numbers_as_string))}')

# print(f"Positive: {', '.join(number for number in numbers_as_string if int(number) >= 0)}")
# print(f"Negative: {', '.join(number for number in numbers_as_string if int(number) < 0)}")
# print(f"Even: {', '.join(number for number in numbers_as_string if int(number) % 2 == 0)}")
# print(f"Odd: {', '.join(number for number in numbers_as_string if int(number) % 2 != 0)}")
