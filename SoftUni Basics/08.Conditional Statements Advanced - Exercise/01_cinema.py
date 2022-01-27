screening_type = input()
rows = int(input())
colums = int(input())

cinema_capacity = rows * colums
ticket_price = 0

if screening_type == 'Premiere':
    ticket_price = 12.00
elif screening_type == 'Normal':
    ticket_price = 7.50
elif screening_type == 'Discount':
    ticket_price = 5.00

total_profit = cinema_capacity * ticket_price
print(f'{total_profit:.2f} leva')