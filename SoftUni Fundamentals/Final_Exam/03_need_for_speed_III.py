number_of_cars = int(input())
cars = {}


for _ in range(number_of_cars):
    cars_input = input().split("|")
    cars[cars_input[0]] = {"mileage": int(cars_input[1]), "fuel": int(cars_input[2])}

while True:
    commands = input().split(" : ")
    if commands[0] == "Stop":
        break

    if commands[0] == "Drive":
        drive_car = commands[1]
        drive_distance = int(commands[2])
        drive_fuel = int(commands[3])
        if drive_fuel > cars[drive_car]["fuel"]:
            print("Not enough fuel to make that ride")
        else:
            cars[drive_car]["mileage"] += drive_distance
            cars[drive_car]["fuel"] -= drive_fuel
            print(f'{drive_car} driven for {drive_distance} kilometers. {drive_fuel} liters of fuel consumed.')

        if cars[drive_car]["mileage"] >= 100000:
            print(f'Time to sell the {drive_car}!')
            del cars[drive_car]

    elif commands[0] == "Refuel":
        refuel_car = commands[1]
        refuel_fuel = int(commands[2])
        refueled = 0
        if cars[refuel_car]["fuel"] <= 75:
            cars[refuel_car]["fuel"] += refuel_fuel
            refueled = refuel_fuel
            if cars[refuel_car]["fuel"] > 75:
                refueled = cars[refuel_car]["fuel"] - (75 + refuel_fuel)
                cars[refuel_car]["fuel"] = 75
        print(f'{refuel_car} refueled with {abs(refueled)} liters')

    elif commands[0] == "Revert":
        revert_car = commands[1]
        revert_kilometers = int(commands[2])
        cars[revert_car]["mileage"] -= revert_kilometers
        if cars[revert_car]["mileage"] <= 10000:
            cars[revert_car]["mileage"] = 10000
        else:
            print(f"{revert_car} mileage decreased by {revert_kilometers} kilometers")

for car in cars:
    print(f'{car} -> Mileage: {cars[car]["mileage"]} kms, Fuel in the tank: {cars[car]["fuel"]} lt.')


# class Piece:
#     def __init__(self, piece_name, composer, key):
#         self.piece_name = piece_name
#         self.composer = composer
#         self.key = key
#
#
# n = int(input())
# pieces = []
#
#
# for _ in range(n):
#     piece_name, composer, key = input().split("|")
#     piece = Piece(piece_name, composer, key)
#     pieces.append(piece)
#
#
# data = input()
#
# while not data == "Stop":
#     command = data.split("|")
#     if command[0] == "Add":
#         piece_name, composer, key = command[1:]
#         if piece_name in [p.piece_name for p in pieces]:
#             print(f"{piece_name} is already in the collection!")
#         else:
#             piece = Piece(piece_name, composer, key)
#             pieces.append(piece)
#             print(f"{piece_name} by {composer} in {key} added to the collection!")
#     elif command[0] == "Remove":
#         piece_name = command[1]
#         if piece_name in [p.piece_name for p in pieces]:
#             piece_to_remove = [p for p in pieces if piece_name == p.piece_name][0]
#             pieces.remove(piece_to_remove)
#             print(f"Successfully removed {piece_name}!")
#         else:
#             print(f"Invalid operation! {piece_name} does not exist in the collection.")
#     elif command[0] == "ChangeKey":
#         piece_name, new_key = command[1:]
#         if piece_name in [p.piece_name for p in pieces]:
#             piece = [p for p in pieces if piece_name == p.piece_name][0]
#             piece.key = new_key
#             print(f"Changed the key of {piece_name} to {new_key}!")
#         else:
#             print(f"Invalid operation! {piece_name} does not exist in the collection.")
#     data = input()
#
# sorted_pieces = sorted(pieces, key=lambda p: (p.piece_name, p.composer))
# for piece in sorted_pieces:
#     print(f"{piece.piece_name} -> Composer: {piece.composer}, Key: {piece.key}")