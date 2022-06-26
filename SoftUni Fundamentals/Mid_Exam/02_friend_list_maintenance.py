def blacklist(name):
    index = usernames.index(name)
    usernames.remove(name)
    usernames.insert(index, "Blacklisted")


def error(index):
    usernames.pop(index)
    usernames.insert(index, "Lost")


def change(index, new_name):
    usernames.pop(index)
    usernames.insert(index, new_name)


usernames = input().split(", ")
usernames_change = usernames.copy()

report = False
lost_due_error = []
blacklisted_count = 0
lost_count = 0

while not report:
    command = input().split()
    if command[0] == "Report":
        report = True
        break

    if command[0] == "Blacklist":
        if command[1] not in usernames:
            print(f'{command[1]} was not found.')
        elif command[1] in usernames:
            blacklist(command[1])
            print(f"{command[1]} was blacklisted.")
            blacklisted_count += 1

    elif command[0] == "Error":
        command[1] = int(command[1])

        if command[1] >= 0 and command[1] < len(usernames):
            if usernames[command[1]] != "Blacklisted":
                if usernames[command[1]] not in lost_due_error:
                    if usernames[command[1]] != "Lost":
                        lost_due_error.append(usernames[command[1]])
                        print(f'{usernames[command[1]]} was lost due to an error.')
                        error(command[1])
                        lost_count += 1


    elif command[0] == "Change":
        command[1] = int(command[1])
        if command[1] >= 0 and command[1] < len(usernames):
            print(f'{usernames[command[1]]} changed his username to {command[2]}.')
            change(command[1], command[2])

print(f'Blacklisted names: {blacklisted_count}')
print(f'Lost names: {lost_count}')
output =' '.join(usernames)
print(output)


# Mike, John, Eddie
# Blacklist Mike
# Error 0
# Report

# Mike, John, Eddie, William
# Error 3
# Error 3
# Change 0 Mike123
# Report

# Mike, John, Eddie, William
# Blacklist Maya
# Error 1
# Change 4 George
# Report