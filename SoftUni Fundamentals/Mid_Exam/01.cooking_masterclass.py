import math

budget = float(input())
students = int(input())
price_flour = float(input())
price_egg = float(input())
price_apron = float(input())

fifth_package = 0
# flour_student = (0 - fifth_package) * price_flour
# eggs_student = 0 * price_egg
# apron_student = 0 * price_apron
# price_per_student = 0


for student in range(1, students + 1):
    # flour_student += 1
    # apron_student += 1
    # eggs_student += 10
    if student % 5 == 0:
        fifth_package += 1

final_price = (price_apron * math.ceil(students + (students * 0.20))) + ((price_egg * 10) * students) + ((students - fifth_package) * price_flour)

if final_price <= budget:
    print(f'Items purchased for {final_price:.2f}$.')
else:
    print(f'{abs(budget - final_price):.2f}$ more needed.')



# 50
# 2
# 1.0
# 0.10
# 10.0

# 100
# 25
# 4.0
# 1.0
# 6.0