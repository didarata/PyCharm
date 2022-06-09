# grade_number = float(input())
#
# if grade_number < 3:
#     print('Fail')
# elif grade_number < 3.50:
#     print('Poor')
# elif grade_number < 4.50:
#     print('Good')
# elif grade_number < 5.50:
#     print('Very Good')
# else:
#     print('Excellent')
#

def great_text():
    grade_number = float(input())

    if grade_number < 3:
        return 'Fail'
    elif grade_number < 3.50:
        return 'Poor'
    elif grade_number < 4.50:
        return 'Good'
    elif grade_number < 5.50:
        return 'Very Good'
    else:
        return 'Excellent'


print(great_text())
