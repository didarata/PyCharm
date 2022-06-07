team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
team_a_count = 11
team_b_count = 11
red_cards = input().split()
player = 0
while player < len(red_cards):
    if red_cards[player] in team_a:
        team_a_count -= 1
    elif red_cards[player] in team_b:
        team_b_count -= 1
    player += 1

print(f'Team A - {team_a_count}; Team B - {team_b_count}')
