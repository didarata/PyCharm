sequence_of_number = input().split()
some_string = input() * 3
sequence_of_string_list = [i for i in some_string]
single_number_sum = 0
character = []
for sequence in sequence_of_number:
    sequence_of_single_number = sequence
    for index in sequence_of_single_number:
        single_number_sum += int(index)
    character.append(sequence_of_string_list[single_number_sum])
    sequence_of_string_list.remove(sequence_of_string_list[single_number_sum])
    single_number_sum = 0


print(*character, sep="")


# numbers = input().split()
# string_text = input()
#
# msg_show = ""
# for num in numbers:
#     find_index = sum(int(s_num) for s_num in num)
#     if find_index > len(string_text):
#         find_index = find_index - len(string_text)
#     msg_show += string_text[find_index]
#     string_text = string_text[:find_index] + string_text[find_index + 1:]
#
# print(msg_show)