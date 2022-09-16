numbers = tuple(map(float, input().split()))

nums_and_occurances = {}
for num in numbers:
    if num not in nums_and_occurances:
        nums_and_occurances[num] = 0
    nums_and_occurances[num] += 1

[print(f"{key} - {value} times") for key, value in nums_and_occurances.items()]


# numbers_to_count = input().split()
#
# result = {float(num): numbers_to_count.count(num) for num in numbers_to_count}
# for number, counter in result.items():
#     print(f"{number:.1f} - {counter} times")

# numbers = ([float(x) for x in input().split()])
# dictionary = {}
#
# for num in numbers:
#     if num not in dictionary:
#         dictionary[num] = 0
#
#     dictionary[num] += 1
#
# for data in dictionary.items():
#     print(f"{data[0]} - {data[1]} times")