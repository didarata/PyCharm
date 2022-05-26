key = int(input())
lines = int(input())
letter = input()
message = []

for n in range(1, lines + 1):
    letter = ord(letter)
    letter += key
    letter = chr(letter)
    message.append(letter)
    if n < lines:
        letter = input()
for message in message:
    print(message, end='')
