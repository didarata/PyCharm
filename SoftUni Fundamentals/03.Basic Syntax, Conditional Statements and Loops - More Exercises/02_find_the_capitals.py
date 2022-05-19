command = input()
list_word = []

for i in range(len(command)):
    if command[i].isupper():
        list_word.append(i)

print(list_word)