actors_name = input()
academy_points = float(input())
judges = int(input())

starting_points = 0
total_points = 0

for i in range(judges):
    judge_name = input()
    judge_points = float(input())
    if judges[0]:
    starting_points += academy_points + ((len(judge_name) * judge_points) / 2)

print(starting_points)

gastia = 0
baba = 0