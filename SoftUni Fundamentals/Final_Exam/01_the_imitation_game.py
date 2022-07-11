def move(number_of_letters):
    for letters in range(number_of_letters):
        letter = decrypted_message.pop(0)
        decrypted_message.append(letter)


def insert(index, value):
    if int(index) > len(decrypted_message):
        decrypted_message.append(value)
    for i in range(len(decrypted_message)):
        if i == int(index):
            decrypted_message.insert(i, value)


def change_all(substring, replacement):
    for index in range(len(decrypted_message)):
        if decrypted_message[index] == substring:
            decrypted_message[index] = replacement


encrypted_message = input()
decrypted_message = list(encrypted_message)
command = input().split('|')

while command[0] != "Decode":

    if command[0] == "Move":
        move(int(command[1]))
    elif command[0] == "Insert":
        insert(command[1], command[2])
    elif command[0] == "ChangeAll":
        change_all(command[1], command[2])

    command = input().split('|')

output =''.join(decrypted_message)
print(f"The decrypted message is: {output}")
