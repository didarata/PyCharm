nights_staying = int(input())
type_of_room = input()
assessment = input()

room_for_one_person = 18.00
apartment = 25.00
president_apartment = 35.00
total_price_nights_staying = 0
discount = 0
total_price_with_discount = 0
total_price = 0

if type_of_room == 'room for one person':
    total_price_nights_staying = (nights_staying - 1) * room_for_one_person
    total_price_with_discount = total_price_nights_staying
elif type_of_room == 'apartment':
    total_price_nights_staying = (nights_staying - 1) * apartment
    if nights_staying < 10:
        total_price_with_discount = total_price_nights_staying - (total_price_nights_staying * 0.30)
    elif nights_staying < 15:
        total_price_with_discount = total_price_nights_staying - (total_price_nights_staying * 0.35)
    elif nights_staying > 16:
        total_price_with_discount = total_price_nights_staying - (total_price_nights_staying * 0.50)
elif type_of_room == 'president apartment':
    total_price_nights_staying = (nights_staying - 1) * president_apartment
    if nights_staying < 10:
        total_price_with_discount = total_price_nights_staying - (total_price_nights_staying * 0.10)
    elif nights_staying < 15:
        total_price_with_discount = total_price_nights_staying - (total_price_nights_staying * 0.15)
    elif nights_staying > 16:
        total_price_with_discount = total_price_nights_staying - (total_price_nights_staying * 0.20)

if assessment == "positive":
    total_price = total_price_with_discount + (total_price_with_discount * 0.25)
elif assessment == 'negative':
    total_price = total_price_with_discount - (total_price_with_discount * 0.10)

print(f'{total_price:.2f}')