not_working_days = int(input())
toms_norm = 30000

working_days = (365 - not_working_days) * 63
holidays = not_working_days * 127
play_time = working_days + holidays
toms_happiness = abs(toms_norm - play_time)
hours = toms_happiness // 60
minutes = toms_happiness % 60

if toms_norm >= play_time:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
elif play_time > toms_norm:

    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')