some_string = input()

command = input().split(' ')

while not command[0] == "Done":

    if command[0] == "TakeOdd":
        some_string = some_string[1:len(some_string):2]
        print(some_string)

    elif command[0] == "Cut":
        index, lenght = int(command[1]), int(command[2])
        some_string = some_string[:index] + some_string[index + lenght:]
        print(some_string)

    elif command[0] == "Substitute":
        if command[1] in some_string:
            some_string = some_string.replace(command[1], command[2])
            print(some_string)
        else:
            print("Nothing to replace!")
    command = input().split(' ')


print(f'Your password is: {some_string}')
