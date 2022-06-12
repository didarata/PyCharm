def all_even_numbers(even_numbers):
    even_list = []
    for even in integer_string:
        if even % 2 == 0:
            even_list.append(even)
    even_number = sum(even_list)
    return even_number


def all_odd_numbers(odd_numbers):
    odd_list = []
    for odd in integer_string:
        if odd % 2 != 0:
            odd_list.append(odd)
    odd_number = sum(odd_list)
    return odd_number


user_string = input()
digits_list = []
for single_digit in user_string:
    digits_list.append(single_digit)
integer_string = [int(i) for i in user_string]

print(f'Odd sum = {all_odd_numbers(integer_string)}, Even sum = {all_even_numbers(integer_string)}')
