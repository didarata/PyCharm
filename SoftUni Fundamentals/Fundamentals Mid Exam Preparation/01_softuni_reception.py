employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
numbers_of_students = int(input())

students_per_hour = employee_one + employee_two + employee_three
hours = 0

while numbers_of_students > 0:
    hours += 1

    if hours % 4 == 0:
        continue

    numbers_of_students -= students_per_hour

print(f'Time needed: {hours}h.')
