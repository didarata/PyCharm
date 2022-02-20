import sys
easter_bread_count = int(input())
max_points = -sys.maxsize
best_baker = ''

for bread in range(1, easter_bread_count + 1):
    baker_name = input()
    total_points_per_baker = 0
    command = input()
    while command != "Stop":
        points = int(command)
        total_points_per_baker += points

        command = input()
    else:
        print(f"{baker_name} has {total_points_per_baker} points.")
        if total_points_per_baker > max_points:
            max_points = total_points_per_baker
            best_baker = baker_name
            print(f'{best_baker} is the new number 1!')

print(f'{best_baker} won competition with {max_points} points!')