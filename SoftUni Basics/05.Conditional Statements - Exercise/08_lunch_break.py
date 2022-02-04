from math import ceil

tv_show = input()
episode_length = int(input())
break_length = int(input())

time_for_lunch = break_length / 8
time_for_relax = break_length / 4
time_left = break_length - time_for_lunch - time_for_relax
diff = abs(episode_length - time_left)

if time_left >= episode_length:
    print(f'You have enough time to watch {tv_show} and left with {ceil(diff)} minutes free time.')
else:
    print(f"You don't have enough time to watch {tv_show}, you need {ceil(diff)} more minutes.")