energy = int(input())
battles_won = 0

while True:
    current_enemy = input()
    if current_enemy == 'End of battle':
        print(f'Won battles: {battles_won}. Energy left: {energy}')
        break
    elif energy <= 0 or energy < int(current_enemy):
        print(f'Not enough energy! Game ends with {battles_won} won battles and {energy} energy')
        break
    if energy >= int(current_enemy):
        battles_won += 1
        energy -= int(current_enemy)
    if battles_won % 3 == 0:
        energy += battles_won
