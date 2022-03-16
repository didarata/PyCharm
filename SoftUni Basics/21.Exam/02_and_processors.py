import math

count_cpu = int(input())
count_workers = int(input())
count_work_days = int(input())

hours_work = count_workers * count_work_days * 8
cpu_made = math.floor(hours_work / 3)
diff = abs(cpu_made - count_cpu)

if cpu_made >= count_cpu:
    print(f'Profit: -> {diff * 110.10:.2f} BGN')
else:
    print(f'Losses: -> {diff * 110.10:.2f} BGN')