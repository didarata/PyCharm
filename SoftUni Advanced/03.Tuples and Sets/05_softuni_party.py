number_of_guests = int(input())

reservation = {input() for _ in range(number_of_guests)}
guests_who_came = input()

while guests_who_came != "END":
    reservation.remove(guests_who_came)
    guests_who_came = input()

print(len(reservation))
print("\n".join(sorted(reservation)))


# n = int(input())
# guests_list = set()
#
# for _ in range(n):
#     guest = input()
#     guests_list.add(guest)
#
# guest_coming = input()
#
# while guest_coming != "END":
#     guests_list.discard(guest_coming)
#     guest_coming = input()
#
# print(len(guests_list))
# print("\n".join(sorted(guests_list)))