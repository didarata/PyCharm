def convert_list_to_round(base_list):
    final_list = list()
    for number in base_list:
        final_number = round(float(number))
        final_list.append(final_number)
    return final_list


input_list = input().split()

print(convert_list_to_round(input_list))
