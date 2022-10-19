from collections import deque
from operator import index

def move(direction_, position_):
    if direction_ == 'up':
        position_[0] -= 1
    elif direction_ == 'down':
        position_[0] += 1
    elif direction_ == 'left':
        position_[1] -= 1
    elif direction_ == 'right':
        position_[1] += 1
    return position_


matrix = []
for _ in range(6):
    matrix.append(input().split())

movement = deque(input().split(", "))
position = []

for row,j in enumerate(matrix):
    for col,el in enumerate(j):
        if el == "E":
            position = row, col

while movement:
    current_command = movement.popleft()
    position = move(current_command, position)
    for row in matrix:
        print(' '.join(row))

# for row in matrix:
#     print(' '.join(row))