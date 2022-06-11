def get_characters(first, second):
    collected_characters = []
    for current_character in range(ord(first) + 1, ord(second)):
        collected_characters.append(chr(current_character))

    return collected_characters


first_character = input()
second_character = input()
result = (get_characters(first_character, second_character))
print(' '.join(result))
