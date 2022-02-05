examp_students = int(input())

d = 0
c = 0
b = 0
a = 0
average_score = 0

for i in range(examp_students):
    grade_from_exam = float(input())
    average_score += grade_from_exam
    if 2.00 <= grade_from_exam <= 2.99:
        d += 1
    elif grade_from_exam <= 3.99:
        c += 1
    elif grade_from_exam <= 4.99:
        b += 1
    else:
        a += 1

d_percentage = (d / examp_students) * 100
c_percentage = (c / examp_students) * 100
b_percentage = (b / examp_students) * 100
a_percentage = (a / examp_students) * 100
total_average_score = average_score / examp_students

print(f'Top students: {a_percentage:.2f}%')
print(f'Between 4.00 and 4.99: {b_percentage:.2f}%')
print(f'Between 3.00 and 3.99: {c_percentage:.2f}%')
print(f'Fail: {d_percentage:.2f}%')
print(f'Average: {total_average_score:.2f}')