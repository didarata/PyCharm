players = input().split()
toss = int(input())

counter = 1

while len(players) != 1:
    for index in range(len(players)):
        if counter == toss:
            player_removed = players.pop(counter)
            print(f"Removed {player_removed}")
            counter = 1
        counter += 1


# Tracy Emily Daniel
# 2