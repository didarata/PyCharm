team_name = input()
type_souvenirs = input()
bought_souvenirs = int(input())

flags = 0
caps = 0
posters = 0
stickers = 0
souvenirs = 0

if team_name == 'Argentina':
    flags += 3.25
    caps += 7.20
    posters += 5.10
    stickers += 1.25
elif team_name == 'Brazil':
    flags += 4.20
    caps += 8.50
    posters += 5.35
    stickers += 1.20
elif team_name == 'Croatia':
    flags += 2.75
    caps += 6.90
    posters += 4.95
    stickers += 1.10
elif team_name == 'Denmark':
    flags += 3.10
    caps += 6.50
    posters += 4.80
    stickers += 0.90

if type_souvenirs == "flags":
    souvenirs = flags
elif type_souvenirs == "caps":
    souvenirs = caps
if type_souvenirs == "posters":
    souvenirs = posters
elif type_souvenirs == "stickers":
    souvenirs = stickers

if team_name == "Argentina" or team_name == "Brazil" or team_name == "Croatia" or team_name == "Denmark":
    if type_souvenirs == "flags" or type_souvenirs == "caps" or type_souvenirs == "posters" or type_souvenirs == "stickers":
        print(f'Pepi bought {bought_souvenirs} {type_souvenirs} of {team_name} for {bought_souvenirs * souvenirs:.2f} lv.')
    else:
        print('Invalid stock!')

elif team_name != "Argentina" or team_name != "Brazil" or team_name != "Croatia" or team_name != "Denmark":
    print("Invalid country!")