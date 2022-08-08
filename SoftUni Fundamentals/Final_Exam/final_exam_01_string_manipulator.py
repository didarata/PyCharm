string = input()

command = input().split(' ')

while not command[0] == "Done":

    if command[0] == "Change":
        char = command[1]
        replacement = command[2]
        for i in string:
            if char == i:
                string = string.replace(i, replacement)
        print(string)

    elif command[0] == "Includes":
        substring = command[1]
        if substring in string:
            print("True")
        else:
            print("False")

    elif command[0] == "End":
        substring = command[1]
        if string.endswith(substring):
            print("True")
        else:
            print("False")

    elif command[0] == "Uppercase":
        string = string.upper()
        print(string)

    elif command[0] == "FindIndex":
        char = command[1]
        index = 0
        for i in string:
            if i == char:
                print(index)
                break
            index += 1

    elif command[0] == "Cut":
        start_index = int(command[1])
        count = int(command[2])
        string = string[start_index: start_index + count]
        print(string)

    command = input().split(' ')
