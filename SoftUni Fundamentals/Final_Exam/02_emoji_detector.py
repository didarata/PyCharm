import re

text = input()
pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"
pattern_threshold = r"[0-9]"
matches = re.finditer(pattern, text)
matches_threshold = re.findall(pattern_threshold, text)

cool_emojis = {}
threshold = 1

for digit in matches_threshold:
    threshold *= int(digit)

current_count = 0

for match in matches:
    for word in match.groups():
        if word.isalpha():
            for letter in word:
                current_count += ord(letter)
            cool_emojis[match.group()] = current_count
            current_count = 0

print(f'Cool threshold: {threshold}')
print(f'{len(cool_emojis)} emojis found in the text. The cool ones are:')
for key, values in cool_emojis.items():
    if values >= threshold:
        print(key)
