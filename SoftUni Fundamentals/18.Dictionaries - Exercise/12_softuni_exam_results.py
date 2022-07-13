student = input().split("-")

exam_results = {}
lenguage = {}

while student[0] != 'exam finished':
    if len(student) == 3:
        name, course, score = student
        if course not in lenguage:
            lenguage[course] = 0
        if name not in exam_results:
            exam_results[name] = 0
        for i in exam_results.values():
            if i <= int(score):
                exam_results[name] = int(score)
        lenguage[course] += 1
    else:
        del exam_results[name]

    student = input().split("-")


print('Results:')
for name, score in exam_results.items():
    print(f'{name} | {score}')
print('Submissions:')
for lenguage, count in lenguage.items():
    print(f'{lenguage} - {count}')
