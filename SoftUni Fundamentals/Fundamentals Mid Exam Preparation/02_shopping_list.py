def urgent(item):
    if item not in initial_list:
        initial_list.insert(0, item)


def unnecessary(item):
    if item in initial_list:
        initial_list.remove(item)


def correct(old_item, new_item):
    if old_item in initial_list:
        index_old = initial_list.index(old_item)
        initial_list.remove(old_item)
        initial_list.insert(index_old, new_item)


def rearrange(item):
    if item in initial_list:
        initial_list.remove(item)
        initial_list.append(item)


initial_list = input().split("!")
go_shopping = False

while not go_shopping:
    commands = input().split()
    if commands[0] == "Go":
        go_shopping = True
        break

    if commands[0] == 'Urgent':
        urgent(commands[1])
    elif commands[0] == 'Unnecessary':
        unnecessary(commands[1])
    elif commands[0] == 'Correct':
        correct(commands[1], commands[2])
    elif commands[0] == 'Rearrange':
        rearrange(commands[1])

output = ', '.join(initial_list)
print(output)

# Tomatoes!Potatoes!Bread
# Unnecessary Milk
# Urgent Tomatoes
# Go Shopping!

# Milk!Pepper!Salt!Water!Banana
# Urgent Salt
# Unnecessary Grapes
# Correct Pepper Onion
# Rearrange Grapes
# Correct Tomatoes Potatoes
# Go Shopping!
