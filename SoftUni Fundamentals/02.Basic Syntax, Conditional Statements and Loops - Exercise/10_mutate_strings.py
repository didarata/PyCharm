first_string = input()
second_string = input()
last_string = first_string

for symbol_index in range(len(second_string)):
    left_part = second_string[:symbol_index + 1]
    right_part = first_string[symbol_index + 1:]
    current_string = left_part + right_part
    if current_string == last_string:
        continue
    print(current_string)
    last_string = current_string

# text1 = input()
# text2 = input()
# transform_list = list(text1)
#
# for letter in range(len(text1)):
#     if transform_list[letter] != text2[letter]:
#         transform_list[letter] = text2[letter]
#         print("".join(transform_list))

