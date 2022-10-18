from collections import deque


def is_bombs_pouch_filled(crafted_bombs):
    for count in crafted_bombs.values():
        if count < 3:
            return False
    return True


bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]

bombs_table = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs'
}

crafted_bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}

while bomb_effects and bomb_casings and not is_bombs_pouch_filled(crafted_bombs):
    bomb_effect = bomb_effects[0]
    bomb_casing = bomb_casings[-1]
    result = bomb_effect + bomb_casing
    
    if result in bombs_table:
        bomb_effects.popleft()
        bomb_casings.pop()
        bomb_type = bombs_table[result]
        crafted_bombs[bomb_type] += 1
    else:
        bomb_casings[-1] -= 5

if is_bombs_pouch_filled(crafted_bombs):
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print('Bomb Effects: empty')

if bomb_casings:
    print(f"Bomb Casing: {', '.join([str(x) for x in bomb_casings])}")
else:
    print('Bomb Casings: empty')

for bomb, count in sorted(crafted_bombs.items()):
    print(f'{bomb}: {count}')


# 5, 25, 25, 115
# 5, 15, 25, 35


# 30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
# 20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10

# https://judge.softuni.org/Contests/Practice/Index/2456#0