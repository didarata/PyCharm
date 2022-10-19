from collections import deque


def move(direction_, position_):
    if direction_ == 'up':
        if position_[0] > 0:
            position_[0] -= 1
        else:
            position_[0] = 5
    elif direction_ == 'down':
        if position_[0] < 5:
            position_[0] += 1
        else:
            position_[0] = 0
    elif direction_ == 'left':
        if position_[1] > 0:
            position_[1] -= 1
        else:
            position_[1] = 5
    elif direction_ == 'right':
        if position_[1] < 5:
            position_[1] += 1
        else:
            position_[1] = 0
    return position_


matrix = []
for _ in range(6):
    matrix.append(input().split())

movement = deque(input().split(", "))
position = []

water = 0
metal = 0
concrete = 0

for row, j in enumerate(matrix):
    for col, el in enumerate(j):
        if el == "E":
            position.append(row)
            position.append(col)

while movement:
    current_command = movement.popleft()
    position = move(current_command, position)

    if matrix[position[0]][position[1]] == "R":
        print(f"Rover got broken at ({position[0]}, {position[1]})")
        break
    elif matrix[position[0]][position[1]] == "W":
        water += 1
        print(f"Water deposit found at ({position[0]}, {position[1]})")
    elif matrix[position[0]][position[1]] == "M":
        metal += 1
        print(f"Metal deposit found at ({position[0]}, {position[1]})")
    elif matrix[position[0]][position[1]] == "C":
        concrete += 1
        print(f"Concrete deposit found at ({position[0]}, {position[1]})")
    elif matrix[position[0]][position[1]] == "-":
        continue

if water != 0 and metal != 0 and concrete != 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

