field = []

first_player_win = False
second_player_win = False
draw = False
#  drawing the game field in separate lists
for field_row in range(3):
    current_row = input().split()
    field.append(current_row)
#  checking each row to see if there is a winner in the row
for row in range(3):
    if field[row][0] == field[row][1] == field[row][2] != "0":
        if field[row][0] == field[row][1] == field[row][2] == "1":
            first_player_win = True
        elif field[row][0] == field[row][1] == field[row][2] == "2":
            second_player_win = True
#  checking each column to see if there is a winner in the column
for col in range(3):
    if field[0][col] == field[1][col] == field[2][col] != "0":
        if field[0][col] == field[1][col] == field[2][col] == "1":
            first_player_win = True
        elif field[0][col] == field[1][col] == field[2][col] == "2":
            second_player_win = True
#  checking left diagonal if there is a winner
if field[0][0] == field[1][1] == field[2][2] != "0":
    if field[0][0] == field[1][1] == field[2][2] == "1":
        first_player_win = True
    elif field[0][0] == field[1][1] == field[2][2] == "2":
        second_player_win = True
#  checking right diagonal if there is a winner
elif field[0][2] == field[1][1] == field[2][0] != "0":
    if field[0][2] == field[1][1] == field[2][0] == "1":
        first_player_win = True
    elif field[0][2] == field[1][1] == field[2][0] == "2":
        second_player_win = True
# if there is no winner found the game is a draw
if not first_player_win and not second_player_win:
    draw = True

if first_player_win:
    print("First player won")
elif second_player_win:
    print("Second player won")
elif draw:
    print("Draw!")
