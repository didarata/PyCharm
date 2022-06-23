some_string = input().split("|")

health = 100
bitcoin = 0
is_alive = True

for i in range((len(some_string))):
    room = some_string[i].split()

    if room[0] == "potion":
        if 100 >= health + int(room[1]):
            print(f'You healed for {int(room[1])} hp.')
        elif 100 < health + int(room[1]):
            print(f'You healed for {100 - health} hp.')

        health += int(room[1])
        if health > 100:
            health = 100
        print(f'Current health: {health} hp.')
    elif room[0] == "chest":
        print(f'You found {room[1]} bitcoins.')
        bitcoin += int(room[1])
    else:
        health -= int(room[1])
        if health > 0:
            print(f'You slayed {room[0]}.')
        else:
            print(f'You died! Killed by {room[0]}.')
            print(f'Best room: {i + 1}')
            is_alive = False
            break

if is_alive:
    print("You've made it!")
    print(f'Bitcoins: {bitcoin}')
    print(f'Health: {health}')
