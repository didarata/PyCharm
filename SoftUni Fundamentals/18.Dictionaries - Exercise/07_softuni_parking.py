number_of_commands = int(input())

register = {}

while number_of_commands > 0:
    commands = input().split(" ")
    number_of_commands -= 1

    if commands[0] == "register":
        name, registration = commands[1], commands[2]
        if name not in register:
            register[name] = registration
            print(f'{name} registered {registration} successfully')
        else:
            print(f"ERROR: already registered with plate number {registration}")

    else:
        name = commands[1]
        if name not in register:
            print(f'ERROR: user {name} not found')
        else:
            print(f'{name} unregistered successfully')
            register.pop(name)

for name, registration in register.items():
    print(f"{name} => {registration}")

# 5
# register John CS1234JS
# register George JAVA123S
# register Andy AB4142CD
# register Jesica VR1223EE
# unregister Andy