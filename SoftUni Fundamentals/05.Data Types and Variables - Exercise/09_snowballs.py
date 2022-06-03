snowballs_made = int(input())

snowball_highest_value = 0
snowballs_weight_highest = 0
snowballs_time_needed_highest = 0
snowballs_quality_highest = 0

for _ in range(snowballs_made):
    snowballs_weight = int(input())
    snowballs_time_needed = int(input())
    snowballs_quality = int(input())
    snowball_current = (snowballs_weight / snowballs_time_needed) ** snowballs_quality

    if snowball_highest_value < snowball_current:
        snowball_highest_value = snowball_current
        snowballs_weight_highest = snowballs_weight
        snowballs_time_needed_highest = snowballs_time_needed
        snowballs_quality_highest = snowballs_quality

print(f'{snowballs_weight_highest} : {snowballs_time_needed_highest} = {int(snowball_highest_value)} ({snowballs_quality_highest})')
