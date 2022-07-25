some_string = input()
generator = input().split(">>>")

while not generator[0] == "Generate":
    if generator[0] == "Contains":
        if generator[1] in some_string:
            print(f"{some_string} contains {generator[1]}")
            # print(some_string)
        else:
            print(f'Substring not found!')

    elif generator[0] == "Flip":
        command, startindex, endindex = generator[1], int(generator[2]), int(generator[3])
        change_part = some_string[startindex:endindex]
        if command == "Upper":
            some_string = some_string.replace(change_part, change_part.upper())
        elif command == "Lower":
            some_string = some_string.replace(change_part, change_part.lower())
        print(some_string)

    elif generator[0] == "Slice":
        startindex, endindex = int(generator[1]), int(generator[2])
        remove_part = some_string[startindex:endindex]
        some_string = some_string.replace(remove_part, "")
        print(some_string)

    generator = input().split(">>>")

print(f'Your activation key is: {some_string}')
