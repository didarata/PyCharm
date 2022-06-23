import math

number_of_students = int(input())
number_of_lectures = int(input())
the_additional_bonus = int(input())
max_student = 0
student_attended = 0

for i in range(1, number_of_students + 1):
    attendance_of_each_student = int(input())
    current_student = attendance_of_each_student / number_of_lectures * (5 + the_additional_bonus)
    if current_student > max_student:
        max_student = current_student
        student_attended = attendance_of_each_student


print(f'Max Bonus: {math.ceil(max_student)}.')
print(f'The student has attended {student_attended} lectures.')

# 5
# 25
# 30
# 12
# 19
# 24
# 16
# 20

# 10
# 30
# 14
# 8
# 23
# 27
# 28
# 15
# 17
# 25
# 26
# 5
# 18