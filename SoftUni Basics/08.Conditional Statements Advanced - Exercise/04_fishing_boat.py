budget = int(input())
season = str(input())
fishermen = int(input())
boat_rent = 0

if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if fishermen <= 6:
    boat_rent -= boat_rent * 0.10
elif 7 <= fishermen <= 11:
    boat_rent -= boat_rent * 0.15
elif fishermen >= 12:
    boat_rent -= boat_rent * 0.25

if season != "Autumn" and fishermen % 2 == 0:
    boat_rent -= boat_rent * 0.05

diff = abs(budget - boat_rent)

if budget >= boat_rent:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")