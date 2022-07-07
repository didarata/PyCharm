import itertools

students_file = {}
while True:
    command = input()
    if ":" not in command:
        break
    command = command.split(':')
    name, id, course = command
    students_file[int(id)] = [name, course]

for id, student in students_file.items():
    names, course = itertools.islice(student, 2)
    if command in student[1]:
        print(f"{names} - {id}")
    elif command == 'programming_basics' and student[1] == 'programming basics':
        print(f"{names} - {id}")


# students = {}
#
# while True:
#     command = input().split(":")
#     if len(command) > 1:
#         name, id, course = command
#         if course not in students:
#             students[course] = {}
#         students[course][id] = name
#     else:
#         break
#
# name_of_course = command[0].replace("_", " ")
# for current_id, current_name in students[name_of_course].items():
#     print(f"{current_name} - {current_id}")
