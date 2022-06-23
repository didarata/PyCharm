def collect(item):
    if command[1] not in items_list:
        items_list.append(item)


def drop(item):
    if command[1] in items_list:
        items_list.remove(item)


def combine_items(items):
    split_items = items.split(':')
    if split_items[0] in items_list:
        index = items_list.index(split_items[0])
        items_list.insert(index + 1, split_items[1])


def renew(item):
    if command[1] in items_list:
        index_renew = items_list.index(item)
        renew = items_list.pop(index_renew)
        items_list.append(renew)


items_list = input().split(", ")
command = input().split(' - ')
while command[0] != "Craft!":
    if command[0] == 'Collect':
        collect(command[1])
    elif command[0] == 'Drop':
        drop(command[1])
    elif command[0] == "Combine Items":
        combine_items(command[1])
    elif command[0] == 'Renew':
        renew(command[1])
    command = input().split(' - ')
output =', '.join(items_list)
print(output)



# items_list = input().split(", ")
# command = input().split(' - ')
#
# while command[0] != "Craft!":
#     combine_items = []
#     if command[0] == 'Collect':
#         if command[1] not in items_list:
#             items_list.append(command[1])
#
#     elif command[0] == 'Drop':
#         if command[1] in items_list:
#             items_list.remove(command[1])
#
#     elif command[0] == "Combine Items":
#         combine_items = command[1].split(':')
#         if combine_items[0] in items_list:
#             index = items_list.index(combine_items[0])
#             items_list.insert(index + 1, combine_items[1])
#
#     elif command[0] == 'Renew':
#         if command[1] in items_list:
#             index_renew = items_list.index(command[1])
#             renew = items_list.pop(index_renew)
#             items_list.append(renew)
#
#     command = input().split(' - ')
#
# output =', '.join(items_list)
# print(output)
