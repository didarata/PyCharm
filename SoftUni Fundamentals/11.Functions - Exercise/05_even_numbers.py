# numbers_as_string = input().split()
# numbers_as_integers = []
# for current_number in numbers_as_string:
#     numbers_as_integers.append(int(current_number))


# numbers_as_integers = [int(s) for s in input().split()]
# is_even = lambda x: x % 2 == 0
# result = list(filter(is_even, numbers_as_integers))
# print(result)


def is_even(number):
    if int(number) % 2 == 0:
        return True
    return False


numbers = input().split()
filtered_numbers = []
for current_number in numbers:
    if is_even(current_number):
        filtered_numbers.append(int(current_number))
print(filtered_numbers)
