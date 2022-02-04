groups_number = int(input())

musala = 0
monblan = 0
kalimandjaro = 0
k2 = 0
everest = 0

total_amount_of_people = 0

for i in range(groups_number):
    people_in_group = int(input())
    total_amount_of_people += people_in_group
    if people_in_group <= 5:
        musala += people_in_group
    elif people_in_group <= 12:
        monblan += people_in_group
    elif people_in_group <= 25:
        kalimandjaro += people_in_group
    elif people_in_group <= 40:
        k2 += people_in_group
    else:
        everest += people_in_group

musala = musala / total_amount_of_people * 100
monblan = monblan / total_amount_of_people * 100
kalimandjaro = kalimandjaro / total_amount_of_people * 100
k2 = k2 / total_amount_of_people * 100
everest = everest / total_amount_of_people * 100

print(f'{musala:.2f}%')
print(f'{monblan:.2f}%')
print(f'{kalimandjaro:.2f}%')
print(f'{k2:.2f}%')
print(f'{everest:.2f}%')