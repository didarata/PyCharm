def remove_numbers(digits, remove):
    final_list = digits
    for index in range(remove):
        final_list.remove(min(final_list))
    return final_list


list_of_integers = input().split()
integers_to_remove = int(input())
list_of_digits = [int(i) for i in list_of_integers]
final_print = remove_numbers(list_of_digits, integers_to_remove)
print(*final_print, sep=", ")
