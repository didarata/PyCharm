player_name = input()
successfull_shots = 0
unsuccessfull_shots = 0
current_points = 301
command = input()
while command != "Retire":
    sector = command
    points_from_last_shot = int(input())
    if sector == "Double":
        points_from_last_shot *= 2
    elif sector == "Triple":
        points_from_last_shot *= 3
    if points_from_last_shot > current_points:
        unsuccessfull_shots += 1
    else:
        successfull_shots += 1
        current_points -= points_from_last_shot
    if current_points == 0:
        break
    command = input()
if current_points == 0:
    print(f"{player_name} won the leg with {successfull_shots} shots.")
else:
    print(f"{player_name} retired after {unsuccessfull_shots} unsuccessful shots.")
