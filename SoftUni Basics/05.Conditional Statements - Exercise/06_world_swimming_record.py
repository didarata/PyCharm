record_secods = float(input())
distance_meters = float(input())
swiming_distance_meter = float(input())

his_time = distance_meters * swiming_distance_meter
drag = (distance_meters // 15) * 12.5
total_time = his_time + drag
diff = abs(record_secods - total_time)

if total_time < record_secods:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {diff:.2f} seconds slower.')