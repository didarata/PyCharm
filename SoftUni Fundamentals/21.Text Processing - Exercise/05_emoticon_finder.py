text = input()

emoticons = []
counter = 0

for symbol in text:
    if counter == 1:
        emoticons.append(symbol)
        counter = 0
    if symbol == ":":
        emoticons.append(symbol)
        counter += 1

for char in range(0, len(emoticons),2):
    name = emoticons[char]
    tag = emoticons[char+1]
    print(name + tag)


# text = input()
# for i in range(len(text)):
#     if text[i] == ':':
#         print(f':{text[i + 1]}')