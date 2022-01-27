hours = int(input())
day_of_the_week = input()

work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 'Saturday']

if day_of_the_week in work_days:
    if 10 <= hours <=18:
        print('open')
    else:
        print('closed')
else:
    print('closed')