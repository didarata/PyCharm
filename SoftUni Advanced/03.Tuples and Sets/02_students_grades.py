# count = int(input())
# students = {}
#
# for _ in range(count):
#     line = tuple(input().split())
#     student, grade = line
#     if student not in students:
#         students[student] = []
#     students[student].append(grade)
#
# for name, grades in students.items():
#     print(f"{name} -> {' '.join(grades)} (avg: {(sum(float(num) for num in grades) / len(grades)):.2f})")


number_of_students = int(input())

result = {}
for student in range(number_of_students):
    student_name, student_grade = input().split()
    result[student_name] = result.get(student_name, list())
    result[student_name].append(f"{float(student_grade):.2f}")

for name, grades in result.items():
    print(f"{name} -> {' '.join(grades)} (avg: {(sum(float(num) for num in grades)/len(grades)):.2f})")



# n = int(input())
# students = {}
#
# for _ in range(n):
#     name, grade_as_str = input().split()
#     grade = float(grade_as_str)
#
#     if name not in students:
#         students[name] = []
#
#     students[name].append(grade)
#
# for data in students.items():
#     print(data)
#     print(f"{data[0]} -> {' '.join([f'{x:.2f}' for x in data[1]])} "
#           f"(avg: {(sum(data[1]) / len(data[1])):.2f})")
#     print(data[1])
#     print(f"{' '.join([f'{x:.2f}' for x in data[1]])}")