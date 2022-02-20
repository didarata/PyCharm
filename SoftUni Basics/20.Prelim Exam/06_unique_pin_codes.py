max_number_one = int(input())
max_number_two = int(input())
max_number_three = int(input())

for num1 in range(2, max_number_one + 1, 2):
    for num2 in range(2, max_number_two + 1):
        for num3 in range(2, max_number_three + 1, 2):
            if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
                print(f"{num1} {num2} {num3}")