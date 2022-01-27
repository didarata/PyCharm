fuel = input()
tank = float(input())


if fuel == 'Diesel' or fuel == 'Gasoline' or fuel == 'Gas':
    if tank >= 25:
        print(f'You have enough {str.lower(fuel)}.')
    elif tank < 25:
        print(f'Fill your tank with {str.lower(fuel)}!')
else:
    print('Invalid fuel!')