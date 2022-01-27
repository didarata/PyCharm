hour = int(input()) * 60
minutes = int(input())

total_minutes = hour + minutes + 15
hour = total_minutes // 60
minutes = total_minutes % 60

if hour <= 23:
    print(f'{hour}:{minutes:02d}')
else:
    print(f'0:{minutes:02d}')