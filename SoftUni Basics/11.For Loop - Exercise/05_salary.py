open_tabs = int(input())
salary = int(input())

penalty = 0
salary_left = 0

for i in range(open_tabs):
    website = input()
    if website == "Facebook":
        penalty += 150
    elif website == "Instagram":
        penalty += 100
    elif website == "Reddit":
        penalty += 50
    else:
        penalty += 0
    if penalty >= salary:
        break

if penalty >= salary:
    print("You have lost your salary.")
else:
    salary_left = salary - penalty
    print(salary_left)