list_of_characters = input().split(', ')
dict_characters = {}

for char in list_of_characters:
    dict_characters[char] = ord(char)

print(dict_characters)

