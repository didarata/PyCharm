first_char = input()
second_char = input()
random_string = input()

first = ord(first_char)
second = ord(second_char)

print(sum([ord(char) for char in random_string if first < ord(char) < second]))
