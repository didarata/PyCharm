number = int(input())
current_year = []
for year in range(number, 99999):
    current_year.append(year)
    year_str = str(current_year)
    first_digit = year_str[1]
    second_digit = year_str[2]
    third_digit = year_str[3]
    fourth_digit = year_str[4]
    fifth_digit = year_str[5]
    if first_digit != second_digit and first_digit != third_digit and first_digit != fourth_digit and \
            first_digit != fifth_digit:
        if second_digit != third_digit and second_digit != fourth_digit and second_digit != fifth_digit:
            if third_digit != fourth_digit and third_digit != fifth_digit:
                if fourth_digit != fifth_digit:
                    print(year)
                    break
    current_year = []
