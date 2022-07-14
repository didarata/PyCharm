# contests_input = input().split(":")
# contests = {}
# students = {}
#
# while contests_input[0] != "end of contests":
#     contest, password_for_contest = contests_input
#     if contest not in contests.keys():
#         contests[contest] = password_for_contest
#
#     contests_input = input().split(":")
#
# students_input = input().split("=>")
#
# while students_input[0] != "end of submissions":
#     contest, password, username, points = students_input
#     if contest in contests.keys() and password in contests.values():
#         if username not in students.keys():
#             students[username] = []
#             students[username].append(contest)
#             students[username].append(int(points))
#         else:
#
#             students.setdefault(username, []).append(contest)
#             students.setdefault(username, []).append(int(points))
#
#     students_input = input().split("=>")
#
# total_points = 0
#
# for student in students.values():
#     for points in student:
#         if str(points).isdigit():
#             total_points += int(points)



contest_add = input()

exams_information = {"contest": {}, "students": {}}
contest_d, students_d = "contest", "students"

while contest_add != "end of contests":
    contest, contest_pass = contest_add.split(":")
    exams_information[contest_d][contest] = contest_pass
    contest_add = input()

submissions = input()
while submissions != "end of submissions":
    contest, contest_pass, contest_user, contest_points = [int(x) if x.isdigit() else x for x in submissions.split("=>")]
    if contest in exams_information[contest_d] and exams_information[contest_d][contest] == contest_pass:
        exams_information[students_d][contest_user] = exams_information[students_d].get(contest_user, {})
        exams_information[students_d][contest_user][contest] = exams_information[students_d][contest_user].get(contest, 0)
        if exams_information[students_d][contest_user][contest] < contest_points:
            exams_information[students_d][contest_user][contest] = contest_points
    submissions = input()


def show_result():
    best_name = ""
    total_points = 0
    for name in exams_information[students_d]:
        score_for_user = sum(exams_information[students_d][name].values())
        if score_for_user > total_points:
            total_points = score_for_user
            best_name = name
    print(f"Best candidate is {best_name} with total {total_points} points.\nRanking:")
    for name in sorted(exams_information[students_d]):
        print(name)
        for contest, points in sorted(exams_information[students_d][name].items(), key=lambda item: -item[1]):
            print(f"#  {contest} -> {points}")


show_result()
