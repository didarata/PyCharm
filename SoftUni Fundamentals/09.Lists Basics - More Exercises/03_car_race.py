sequence_of_numbers = input().split()


finish_line = len(sequence_of_numbers) // 2
left_car = sequence_of_numbers[0:finish_line]
right_car = sequence_of_numbers[:finish_line:-1]

left_car_sum_int = [int(i) for i in left_car]
right_car_sum_int = [int(i) for i in right_car]

left_car_test_final_sum = 0
for i in left_car_sum_int:
    if i != 0:
        left_car_test_final_sum += i
    else:
        left_car_test_final_sum *= 0.8

right_car_final_sum = 0
for x in right_car_sum_int:
    if x != 0:
        right_car_final_sum += x
    else:
        right_car_final_sum *= 0.8

if left_car_test_final_sum < right_car_final_sum:
    print(f"The winner is left with total time: {left_car_test_final_sum:.1f}")
else:
    print(f"The winner is right with total time: {right_car_final_sum:.1f}")
