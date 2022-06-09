def number_of_beggars(single_string, count_beggars):
    integer_string = [int(i) for i in single_string]
    final_result = list()
    counter_of_index = 0
    while counter_of_index < count_beggars:
        sum_for_current_beggar = 0
        for current_index in range(counter_of_index, len(integer_string), count_beggars):
            sum_for_current_beggar += integer_string[current_index]
        counter_of_index += 1
        final_result.append(sum_for_current_beggar)
    return final_result


new_string = input().split(', ')
new_count_beggars = int(input())
print(number_of_beggars(new_string, new_count_beggars))


# list_of_money = input().split(', ')
# beggars = int(input())
# number_beggars = []
# for beggar in range(beggars):
#     money_for_current_beggar = list_of_money[beggar:len(list_of_money):beggars]
#     sum_for_current_beggar = sum(int(x) for x in money_for_current_beggar)
#     number_beggars.append(sum_for_current_beggar)
# print(number_beggars)

# -----------------------------------------------
#
# list_of_numbers = [int(x) for x in input().split(", ")]
# number_of_beggars = int(input())
#
# final_list = []
#
# for beggar in range(number_of_beggars):
#     current_list = []
#     for current_beggar in range(beggar, len(list_of_numbers), number_of_beggars):
#         current_list.append(list_of_numbers[current_beggar])
#     final_list.append(sum(current_list))
#
# print(final_list)
#
# -----------------------------------------------------
#
# list_of_integer = input().split(", ")
# beggars = [0] * int(input())
# index = 0
#
# for number in list_of_integer:
#     current_number = int(number)
#     beggars[index] += current_number
#     index += 1
#     if index == len(beggars):
#         index = 0
#
# print(beggars)
