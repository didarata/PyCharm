km = int(input())
time_of_day = input()
total_amount = 0

if km < 20 and time_of_day == 'day':
    total_amount = (km * 0.79) + 0.70
    print(f'{total_amount:.2f}')
elif km < 20 and time_of_day == "night":
    total_amount = (km * 0.90) + 0.70
    print(f'{total_amount:.2f}')
elif km < 100:
    total_amount = km * 0.09
    print(f'{total_amount:.2f}')
elif km >= 100:
    total_amount = km * 0.06
    print(f'{total_amount:.2f}')