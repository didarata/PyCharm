first_number = int(input())
second_number = int(input())

sum = second_number % first_number
if sum == 0:
    print(second_number)
elif sum != 0:
    result = second_number - sum
    print(result)
