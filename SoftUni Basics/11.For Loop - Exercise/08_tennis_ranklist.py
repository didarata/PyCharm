tournaments_count = int(input())
starting_ranklist_points = int(input())

w = 2000
f = 1200
sf = 720
current_points = 0
won_tournaments = 0

for i in range(tournaments_count):
    tournaments_points = input()
    if tournaments_points == "W":
        current_points += 2000
        won_tournaments += 1
    elif tournaments_points == "F":
        current_points += 1200
    elif tournaments_points == "SF":
        current_points += 720

current_points += starting_ranklist_points
average_points = (current_points - starting_ranklist_points) / tournaments_count
procentage_won_tournaments = (won_tournaments / tournaments_count) * 100

print(f'Final points: {current_points}')
print(f'Average points: {int(average_points)}')
print(f'{procentage_won_tournaments:.2f}%')