name = input()

while name != "Welcome!":
    total = 0
    if name == 'Voldemort':
        print(f'You must not speak of that name!')
        break
    for char in range(len(name)):
        total += 1
    if total < 5:
        print(f"{name} goes to Gryffindor.")
    elif total == 5:
        print(f"{name} goes to Slytherin.")
    elif total == 6:
        print(f'{name} goes to Ravenclaw.')
    elif total > 6:
        print(f'{name} goes to Hufflepuff.')

    name = input()
if name == "Welcome!":
    print("Welcome to Hogwarts.")
