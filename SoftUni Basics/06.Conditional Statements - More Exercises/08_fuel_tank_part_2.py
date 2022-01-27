type_of_fuel = input()
quantity_fuel = float(input())
club_member = input()

diesel_price = 2.33
gasoline_price = 2.22
lpg = 0.93
total_price = 0

if type_of_fuel == "Gas" and club_member == "Yes":
    lpg -= 0.08
    total_price = quantity_fuel * lpg
elif type_of_fuel == "Gas" and club_member == "No":
    total_price = quantity_fuel * lpg

if type_of_fuel == "Gasoline" and club_member == "Yes":
    gasoline_price -= 0.18
    total_price = quantity_fuel * gasoline_price
elif type_of_fuel == "Gasoline" and club_member == "No":
    total_price = quantity_fuel * gasoline_price

if type_of_fuel == "Diesel" and club_member == "Yes":
    diesel_price -= 0.12
    total_price = quantity_fuel * diesel_price
elif type_of_fuel == "Diesel" and club_member == "No":
    total_price = quantity_fuel * diesel_price

if 20 <= quantity_fuel <= 25:
    total_price -= total_price * 0.08
elif quantity_fuel > 25:
    total_price -= total_price * 0.10

print(f'{total_price:.2f} lv.')