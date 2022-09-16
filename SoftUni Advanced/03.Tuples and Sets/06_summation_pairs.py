# pairs_of_numbers = [int(num) for num in input().split()]
#
# target_number = int(input())
# result_print = set()
# total_iterations = 0
# for pos, number_one in enumerate(pairs_of_numbers, 1):
#     for number_two in pairs_of_numbers[pos:]:
#         total_iterations += 1
#         if number_one + number_two == target_number:
#             result_print.add((number_one, number_two))
#             print(f"{number_one} + {number_two} = {target_number}")
#
# print(f"Iterations done: {total_iterations}")
# if result_print:
#     print(*result_print, sep="\n")



numbers = list(map(int, input().split()))
target = int(input())

while numbers:
    i = 0
    first = numbers.pop(0)

    while i < len(numbers):
        second = numbers[i]

        if first + second == target:
            print(f"{first} + {second} = {target}")
            if i + 1 >= len(numbers):
                break
            else:
                first = numbers[i + 1]
                numbers.pop(i)
        i += 1