students = int(input())

top_students = 0
good_students = 0
average_students = 0
bad_students = 0
average_grade = 0

for i in range(students):
    grade = float(input())
    average_grade += grade
    if 2 <= grade <= 2.99:
        bad_students += 1
    elif 3 <= grade <= 3.99:
        average_students += 1
    elif 4 <= grade <= 4.99:
        good_students += 1
    elif grade >= 5:
        top_students += 1

top_students = top_students / students * 100
good_students = good_students / students * 100
average_students = average_students / students * 100
bad_students = bad_students / students * 100
average_grade = average_grade / students


print(f'Top students: {top_students:.2f}%')
print(f'Between 4.00 and 4.99: {good_students:.2f}%')
print(f'Between 3.00 and 3.99: {average_students:.2f}%')
print(f'Fail: {bad_students:.2f}%')
print(f'Average: {average_grade:.2f}')