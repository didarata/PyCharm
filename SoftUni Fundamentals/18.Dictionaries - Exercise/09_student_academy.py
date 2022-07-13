number_of_students = int(input())

academy = {}

for i in range(number_of_students):
    student = input()
    grade = input()
    if student not in academy:
        academy[student] = []
    academy[student].append(grade)

for i in academy.keys():
    name = i
    average_grade = 0
    count = 0
    for i in academy[name]:
        average_grade += float(i)
        count += 1
    if (average_grade / count) >= 4.50:
        print(f'{name} -> {(average_grade / count):.2f}')


# lazi print
# for name, score in students.items():
#     avg_score = sum(score) / len(score)
#     if avg_score >= 4.50:
#         print(f'{name} -> {avg_score:.2f}')


# 5
# John
# 5.5
# John
# 4.5
# Alice
# 6
# Alice
# 3
# George
# 5