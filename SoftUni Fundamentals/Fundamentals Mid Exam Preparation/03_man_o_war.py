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




# 12>13>11>20>66
# 12>22>33>44>55>32>18
# 70
# Fire 2 11
# Fire 8 100
# Defend 3 6 11
# Defend 0 3 5
# Repair 1 33
# Status
# Retire


# 2>3>4>5>2
# 6>7>8>9>10>11
# 20
# Status
# Fire 2 3
# Defend 0 4 11
# Repair 3 18
# Retire