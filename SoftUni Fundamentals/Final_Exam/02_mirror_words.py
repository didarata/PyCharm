import re

pattern_one = r"([@#])(?P<first>[A-Za-z]{3,})\1\1(?P<second>[A-Za-z]{3,})\1"

text = input()
matches_one = re.finditer(pattern_one, text)

word_counter = 0
mirrored_words = []
for match in matches_one:
    first_word = match.group("first")
    second_word = match.group("second")
    second_word_reversed = second_word[::-1]
    word_counter += 1
    if first_word == second_word_reversed:
        mirrored_words.append(f"{first_word} <=> {second_word}")

if word_counter > 0:
    print(f"{word_counter} word pairs found!")
else:
    print("No word pairs found!")

if len(mirrored_words) > 0:
    print(f'The mirror words are:')
    print(", ". join(mirrored_words))
else:
    print("No mirror words!")
