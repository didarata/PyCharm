days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
current_plunder = 0

for day in range(1, days + 1):
    current_plunder += daily_plunder
    if day % 3 == 0:
        current_plunder += daily_plunder * 0.50
    if day % 5 == 0:
        current_plunder -= current_plunder * 0.30

percentage_plunder = (current_plunder / expected_plunder) * 100

if current_plunder >= expected_plunder:
    print(f'Ahoy! {current_plunder:.2f} plunder gained.')
elif current_plunder < expected_plunder:
    print(f'Collected only {percentage_plunder:.2f}% of the plunder.')
