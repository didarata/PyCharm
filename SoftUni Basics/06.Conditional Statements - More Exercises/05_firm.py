hours_need = int(input())
days_company_has = int(input())
count_workers_working_overtime = int(input())

hours_for_work = (days_company_has * 0.9) * 8
overtime_workers_time = count_workers_working_overtime * (2 * days_company_has)
total_hours = int(hours_for_work + overtime_workers_time)
time_left = abs(hours_need - total_hours)

if total_hours >= hours_need:
    print(f'Yes!{time_left} hours left.')
else:
    print(f'Not enough time!{time_left} hours needed.')