n = int(input())
cars = set()

for _ in range(n):
    command, car = input().split(", ")

    if command == "IN":
        cars.add(car)

    elif command == "OUT":
        cars.discard(car)

if cars:
    print("\n".join(cars))

else:
    print("Parking Lot is Empty")




# car_numbers = int(input())
#
# parking_lot = set()
# for car in range(car_numbers):
#     direction, car_plate_number = input().split(", ")
#
#     if "IN" == direction:
#         parking_lot.add(car_plate_number)
#
#     elif "OUT" == direction and car_plate_number in parking_lot:
#         parking_lot.remove(car_plate_number)
#
#
# if parking_lot:
#     print('\n'.join(parking_lot))
# else:
#     print("Parking Lot is Empty")
