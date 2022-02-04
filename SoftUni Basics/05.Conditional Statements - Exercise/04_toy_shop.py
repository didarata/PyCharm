trip_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

number_of_toys = puzzles + talking_dolls + teddy_bears + minions + trucks

puzzles = puzzles * 2.60
talking_dolls = talking_dolls * 3
teddy_bears = teddy_bears * 4.10
minions = minions * 8.20
trucks = trucks * 2

total_price_toys = puzzles + talking_dolls + teddy_bears + minions + trucks

money_left = 0

if number_of_toys >= 50:
    total_price_toys -= total_price_toys * 0.25

rent = total_price_toys * 0.10
earnings = total_price_toys - rent

money_left = abs(earnings - trip_price)

if earnings >= trip_price:
    print(f'Yes! {money_left:.2f} lv left.')
else:
    print(f'Not enough money! {money_left:.2f} lv needed.')