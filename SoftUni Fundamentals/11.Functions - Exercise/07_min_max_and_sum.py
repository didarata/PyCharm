def minimal(min_number):
    return min(integer_list)


def maximum(max_number):
    return max(integer_list)


def sum_of_all(sum_number):
    return sum(integer_list)


sequence_of_numbers = input().split()
integer_list = [int(i) for i in sequence_of_numbers]

print(f"The minimum number is {minimal(integer_list)}")
print(f"The maximum number is {maximum(integer_list)}")
print(f'The sum number is: {sum_of_all(integer_list)}')
