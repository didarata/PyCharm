def move(direction, moving):
    if direction == 'up':
        if moving[0] > 0:
            moving[0] -= 1
    elif direction == 'down':
        if moving[0] < 5:
            moving[0] += 1
    elif direction == 'left':
        if moving[1] > 0:
            moving[1] -= 1
    elif direction == 'right':
        if moving[1] < 5:
            moving[1] += 1

    return moving


matrix = []
racing_track = int(input())
racing_number = input()

for _ in range(racing_track):
    matrix.append(input().split())

start = [0, 0]

command = input()

distance_covered = 0

position = []

while True:

    position = move(command, start)

    if command == "End":
        print(f'Racing car {racing_number} DNF.')
        matrix[position[0]][position[1]] = "C"
        break

    if matrix[position[0]][position[1]] == "F":
        distance_covered += 10
        print(f'Racing car {racing_number} finished the stage!')
        matrix[position[0]][position[1]] = "C"
        break

    elif matrix[position[0]][position[1]] == ".":
        distance_covered += 10

    elif matrix[position[0]][position[1]] == "T":
        distance_covered += 30
        matrix[position[0]][position[1]] = "."

        for row, j in enumerate(matrix):
            for col, el in enumerate(j):
                if el == "T":
                    start = [row, col]

                    matrix[start[0]][start[1]] = "."

    command = input()

if distance_covered >= 0:
    print(f'Distance covered {distance_covered} km.')

for row in matrix:
    print(*row, sep="")


# 5
# 01
# . . . . .
# . . . T .
# . . . . .
# . T . . .
# . . F . .
# End
# right
# right
# right
# down
# right
# up
# down
# right
# up
# End