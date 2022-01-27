skumria_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_price = (skumria_price + (skumria_price * 0.6)) * palamud_kg
safrid_price = (caca_price + (caca_price* 0.8)) * safrid_kg
midi_price = midi_kg * 7.50
total_price = palamud_price + safrid_price + midi_price

print(f"{total_price:.2f}")