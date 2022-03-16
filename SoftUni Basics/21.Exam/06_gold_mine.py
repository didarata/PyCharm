locations = int(input())


for i in range(1 , locations + 1):
    average_gold_per_day = float(input())
    days_digging = int(input())
    total_average_gold = 0
    for gold in range(1, days_digging + 1):
        average_gold_per_day_next = float(input())
        total_average_gold += average_gold_per_day_next / days_digging
        # total_average_gold += average_gold_per_day / days_digging

    if average_gold_per_day <= total_average_gold:
        print(f'Good job! Average gold per day: {total_average_gold:.2f}.')
    else:
        print(f'You need {abs(average_gold_per_day - total_average_gold):.2f} gold.')