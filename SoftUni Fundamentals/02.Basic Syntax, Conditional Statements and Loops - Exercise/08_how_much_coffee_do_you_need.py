command = input()
coffees = 0
while command != 'END':
    if command == 'cat' or command == 'dog' or command == 'coding' or command == 'movie':
        coffees += 1
    if command == 'CAT' or command == 'DOG' or command == 'CODING' or command == 'MOVIE':
        coffees += 2
    command = input()
if coffees <= 5:
    print(coffees)
else:
    print("You need extra sleep")
