def check_chairs(numbers_of_rooms):
    total_free_chairs = 0
    needed_chairs = 0
    for number_of_room in range(1, numbers_of_rooms + 1):
        free_chairs, visitors = input().split()
        differance = len(free_chairs) - int(visitors)
        if differance >= 0:
            total_free_chairs += differance
        else:
            needed_chairs += abs(differance)
            print(f'{abs(differance)} more chairs needed in room {number_of_room}')
    return total_free_chairs, needed_chairs


numbers_of_rooms = int(input())
total_free_chairs, needed_chairs = check_chairs(numbers_of_rooms)
if total_free_chairs >= needed_chairs:
    print(f'Game On, {total_free_chairs} free chairs left')
