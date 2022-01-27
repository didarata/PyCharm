day = int(input())

days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if 1 <= day <= 7:
    day -= 1
    print(days_of_the_week[day])
else:
    print("Error")