quantity_of_decoration = int(input())
days_left_until_christmas = int(input())

istrue = 1 <= quantity_of_decoration <= 100 and 1 <= days_left_until_christmas <= 100
total_cost = 0
current_cost = 0
total_spirit = 0
while istrue:
    for day in range(1, days_left_until_christmas + 1):
        if day % 11 == 0:
            quantity_of_decoration = quantity_of_decoration + 2
        if day % 10 == 0:
            total_spirit -= 20
            current_cost += 5 + 3 + 15
        if day % 2 == 0:
            current_cost += 2 * quantity_of_decoration
            total_spirit += 5
        if day % 3 == 0:
            current_cost += (5 * quantity_of_decoration) + (3 * quantity_of_decoration)
            total_spirit += 3 + 10
        if day % 5 == 0:
            current_cost += 15 * quantity_of_decoration
            total_spirit += 17
            if day % 3 == 0:
                total_spirit += 30
        total_cost += current_cost
        current_cost = 0
    break
if days_left_until_christmas % 10 == 0:
    total_spirit -= 30
print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')