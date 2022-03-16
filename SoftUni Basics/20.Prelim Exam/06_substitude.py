k = int(input())
l = int(input())
m = int(input())
n = int(input())

current_combination = 0
current_num1 = 0
current_num2 = 0
current_num3 = 0
current_num4 = 0

for num4 in range(9, n - 1, - 1):
    if num4 % 2 != 0:
        current_num4 = num4
    for num3 in range(m, 8 + 1):
        if num3 % 2 == 0:
            current_num3 = num3
        for num2 in range(9, l - 1, - 1):
            if num2 % 2 != 0:
                current_num2 = num2
            for num1 in range(k, 8 + 1):
                if num1 % 2 == 0:
                    current_num1 = num1
    current_combination += 1



    # for num4 in range(9, n - 1, - 1):
    #     if num4 % 2 != 0:
    #         current_num4 = num4
    #     for num3 in range(m, 8 + 1):
    #         if num3 % 2 == 0:
    #             current_num3 = num3
    #         for num2 in range(9, l - 1, - 1):
    #             if num2 % 2 != 0:
    #                 current_num2 = num2
    #             for num1 in range(k, 8 + 1):
    #                 if num1 % 2 == 0:
    #                     current_num1 = num1
    #
    # for num1 in range(k, 8 + 1):
    #     if num1 % 2 == 0:
    #         current_num1 = num1
    #     for num2 in range(9, l - 1, - 1):
    #         if num2 % 2 != 0:
    #             current_num2 = num2
    #         for num3 in range(m, 8 + 1):
    #             if num3 % 2 == 0:
    #                 current_num3 = num3
    #             for num4 in range(9, n - 1, - 1):
    #                 if num4 % 2 != 0:
    #                     current_num4 = num4