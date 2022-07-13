command = input().split(" : ")

courses = {}

while command[0] != "end":

    course, name = command[0], command[1]
    if course not in courses:
        courses[course] = []
        courses[course].append(name)
    else:
        courses.setdefault(course, []).append(name)

    command = input().split(" : ")

for course in courses.keys():
    print(f"{course}: {len(courses[course])}")
    for name in courses[course]:
        print(f'-- {name}')



# Programming Fundamentals : John Smith
# Programming Fundamentals : Linda Johnson
# JS Core : Will Wilson
# Java Advanced : Harrison White
# end