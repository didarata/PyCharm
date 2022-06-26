def add(phone):
    if phone not in items_list:
        items_list.append(phone)


def remove(phone):
    if phone in items_list:
        items_list.remove(phone)


def bonus_phone(phones):
    split_phones = phones.split(':')
    if split_phones[0] in items_list:
        index = items_list.index(split_phones[0])
        items_list.insert(index + 1, split_phones[1])


def last(phone):
    if phone in items_list:
        index_renew = items_list.index(phone)
        renew = items_list.pop(index_renew)
        items_list.append(renew)


items_list = input().split(", ")

is_end = False

while not is_end:
    command = input().split(' - ')
    if command[0] == "End":
        is_end = True
        break

    if command[0] == "Add":
        add(command[1])
    elif command[0] == "Remove":
        remove(command[1])
    elif command[0] == "Bonus phone":
        bonus_phone(command[1])
    elif command[0] == "Last":
        last(command[1])



output =', '.join(items_list)
print(output)



# SamsungA50, MotorolaG5, IphoneSE
# Add - Iphone10
# Remove - IphoneSE
# End

# HuaweiP20, XiaomiNote
# Remove - Samsung
# Bonus phone - XiaomiNote:Iphone5
# End