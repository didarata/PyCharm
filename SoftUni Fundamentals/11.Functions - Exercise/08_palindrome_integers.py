def palindrome_integer(number):
    if not isinstance(number, int):
        return False
    elif str(number) == str(number)[::-1]:
        return True
    else:
        return False


list_of_strings = input().split(", ")
list_of_integers = [int(i) for i in list_of_strings]

for single_number in list_of_integers:
    print(palindrome_integer(single_number))
