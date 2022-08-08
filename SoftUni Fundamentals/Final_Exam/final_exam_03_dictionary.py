dictionary = {}

words_and_definitions = input().split(" | ")

for word in words_and_definitions:
    word = word.split(":")
    if word[0] not in dictionary:
        dictionary[word[0]] = [word[1]]
    else:
        dictionary[word[0]].append(word[1])

only_words = input().split(" | ")

command = input()

if command == "Test":
    for w in only_words:
        for key, value in dictionary.items():
            if w == key:
                print(f"{key}:")
                for index in range(len(value)):
                    print(f'-{value[index].strip()}')


elif command == "Hand Over":
    for key in dictionary.keys():
        print(key, end=" ")
