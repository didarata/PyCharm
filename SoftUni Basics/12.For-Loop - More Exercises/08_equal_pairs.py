n = int(input())

previous_number = 0

for i in range(1, n):
    first_number = int(input())
    second_number = int(input())
    current_pair = first_number + second_number
    previous_number = current_pair
    if current_pair == previous_number:
        print('YES')
    else:
        print('NO')



UNFINISHED


