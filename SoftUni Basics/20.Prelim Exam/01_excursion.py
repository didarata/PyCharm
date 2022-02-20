people_in_the_group = int(input())
nights_count = int(input())
card_for_transport_count = int(input())
tickets_for_museum_count = int(input())

price_per_night = 20
card_for_transport = 1.60
ticket_for_museum = 6

total_nights_per_person = nights_count * price_per_night
total_transport_per_person = card_for_transport_count * card_for_transport
total_museum =  tickets_for_museum_count * ticket_for_museum
total_price_per_person = total_nights_per_person + total_transport_per_person + total_museum
total_price_for_all = total_price_per_person * people_in_the_group
total_sum = total_price_for_all + (total_price_for_all * 0.25)
print(f'{total_sum:.2f}')