single_string = input().split(',')
single_integer_list = [int(i) for i in single_string]
regular_list = []
zeros_list = []
for index in single_integer_list:
    if index == 0:
        zeros_list.append(index)
    else:
        regular_list.append(index)

print(regular_list + zeros_list)
