some_string = list(map(int, input().split("@")))
command = input().split()
command_jump = int(command[1])
corrent_position = 0
last_position = 0
fail_count = 0

love_on = True

while love_on:
    command_jump = int(command[1])
    if command_jump + corrent_position < len(some_string):
        current_index = some_string[command_jump + corrent_position]
        some_string[command_jump + corrent_position] -= 2
        corrent_position = command_jump + corrent_position

    else:
        some_string[0] -= 2
        corrent_position = 0

    command = input().split()
    if command[0] == "Love!":
        love_on = False

    if -1 < some_string[corrent_position] <= 0:
        print(f"Place {corrent_position} has Valentine's day.")
    elif some_string[corrent_position] <= -2:
        print(f"Place {corrent_position} already had Valentine's day.")

for i, number in enumerate(some_string):
    if number > 0:
        fail_count += 1

print(f"Cupid's last position was {corrent_position}.")
if fail_count == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {fail_count} places.")


# 10@10@10@2
# Jump 1
# Jump 2
# Love!



# 2@4@2
# Jump 2
# Jump 2
# Jump 8
# Jump 3
# Jump 1
# Love!