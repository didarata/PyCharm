letters = input()
replaced_chars = []

for char in letters:
    if len(replaced_chars) == 0:
        replaced_chars.append(char)
    elif char != replaced_chars[-1]:
        replaced_chars.append(char)

print(''.join(replaced_chars))
