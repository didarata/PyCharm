count_pages = int(input())
pages_per_hour = int(input())
days = int(input())

time_to_read = count_pages / pages_per_hour
total_time = time_to_read // days

print(total_time)