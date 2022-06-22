pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
maximum_healt_capacity = int(input())

need_repair = 0
game_on = True
is_sunk_pirate = False
is_sunk_warship = False

while game_on:
    command = input().split()
    command_string = command.pop(0)
    command = list(map(int, command))

    if command_string == "Retire":
        game_on = False
        break

    if command_string == 'Fire':
        if 0 <= command[0] < len(warship):
            warship[command[0]] = warship[command[0]] - command[1]
            if warship[command[0]] <= 0:
                is_sunk_pirate = True
                game_on = False
    elif command_string == 'Defend':
        if 0 <= command[0] < len(pirate_ship) and 0 <= command[1] < len(pirate_ship):
            for hit in range(command[0], command[1] + 1):
                pirate_ship[hit] = pirate_ship[hit] - command[2]
            for sunk in range(command[0], command[1] + 1):
                if pirate_ship[sunk] <= 0:
                    is_sunk_warship = True
                    game_on = False
    elif command_string == 'Repair':
        if 0 <= command[0] < len(pirate_ship):
            pirate_ship[command[0]] = pirate_ship[command[0]] + command[1]
            if pirate_ship[command[0]] >= maximum_healt_capacity:
                pirate_ship[command[0]] = maximum_healt_capacity
    elif command_string == 'Status':
        need_repair = 0
        for section in range(len(pirate_ship)):
            section_for_repair = maximum_healt_capacity * 0.2
            if pirate_ship[section] < section_for_repair:
                need_repair += 1
        if need_repair:
            print(f'{need_repair} sections need repair.')

if is_sunk_pirate:
    print('You won! The enemy ship has sunken.')
elif is_sunk_warship:
    print('You lost! The pirate ship has sunken.')
else:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(warship)}')



# pirate_ship, warship, maximum_health = [int(n) for n in input().split(">")], [int(n) for n in input().split(">")], int(
#     input())
# command = input()
#
#
# def status_ship():
#     repair_counter = 0
#     for hp in pirate_ship:
#         if ((hp / maximum_health) * 100) < 20.00:
#             repair_counter += 1
#     if repair_counter:
#         print(f"{repair_counter} sections need repair.")
#
#
# def fire_ship(index, damage):
#     if 0 <= index < len(warship):
#         warship[index] -= damage
#         if warship[index] <= 0:
#             print(f"You won! The enemy ship has sunken.")
#             exit()
#
#
# def defend_ship(start_index, end_index, damage):
#     if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
#         for index in range(start_index, end_index + 1):
#             pirate_ship[index] -= damage
#             if pirate_ship[index] <= 0:
#                 print(f"You lost! The pirate ship has sunken.")
#                 exit()
#
#
# def repair_ship(index, health):
#     if 0 <= index < len(pirate_ship):
#         pirate_ship[index] += health
#         if pirate_ship[index] > maximum_health:
#             pirate_ship[index] = maximum_health
#
#
# while command != "Retire":
#     command = command.split()
#     type_command = command[0]
#     if type_command == "Status":
#         status_ship()
#     else:
#         index_ship, damage_or_health_ship = int(command[1]), int(command[2])
#     if type_command == "Fire":
#         fire_ship(index_ship, damage_or_health_ship)
#     elif type_command == "Defend":
#         defend_ship(index_ship, damage_or_health_ship, int(command[-1]))
#     elif type_command == "Repair":
#         repair_ship(index_ship, damage_or_health_ship)
#     command = input()
#
# if len(pirate_ship) and len(warship) > 0:
#     print(f"Pirate ship status: {sum(pirate_ship)}")
#     print(f"Warship status: {sum(warship)}")