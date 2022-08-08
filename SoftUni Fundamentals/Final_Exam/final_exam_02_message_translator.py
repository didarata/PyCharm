import re

n = int(input())

pattern = r"(!)([A-Z]{1}[a-z]{2,})\1:[[A-Za-z]{8,}]"

for _ in range(n):
    valid_string = input()

    if re.match(pattern, valid_string):
        output = []

        valid_string = valid_string.split(":")
        command = valid_string[0]
        string = valid_string[1]

        string = string[1:-1]
        command = command[1:-1]

        for char in string:
            number = ord(char)
            output.append(number)
        print(f"{command}: {' '.join(map(str, output))}")

    else:
        print("The message is invalid")
