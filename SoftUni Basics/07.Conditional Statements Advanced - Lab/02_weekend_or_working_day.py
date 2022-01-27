day_of_the_week = input()

work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekends = ["Saturday", "Sunday"]

if day_of_the_week in work_days:
    print('Working day')
elif day_of_the_week in weekends:
    print('Weekend')
else:
    print('Error')