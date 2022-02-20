start_number = int(input())
end_number = int(input())

# всички числа от start_number до end_number
for number in range (start_number, end_number + 1):
    # проверка дали всички цифри от числото за нечетни
    # 4567
    units = number % 10 # единиците
    tens = number // 10 % 10 # десетиците
    hundreds = number // 100 % 10 # стотиците
    thousands = number // 1000 # хилядни

    if units % 2 != 0 and tens % 2 != 0 and hundreds % 2 != 0 and thousands % 2 != 0:
        print(number, end=" ")

# start = int(input())
# end = int(input())
#
# str_start = str(start)
# str_end = str(end)
#
# for i in range(int(str_start[0]), int(str_end[0]) + 1):
#     if i % 2 == 0:
#         continue
#     for j in range(int(str_start[1]), int(str_end[1]) + 1):
#         if j % 2 == 0:
#             continue
#         for k in range(int(str_start[2]), int(str_end[2]) + 1):
#             if k % 2 == 0:
#                 continue
#             for l in range(int(str_start[3]), int(str_end[3]) + 1):
#                 if l % 2 == 0:
#                     continue
#                 print(f'{i}{j}{k}{l}', end=' ')