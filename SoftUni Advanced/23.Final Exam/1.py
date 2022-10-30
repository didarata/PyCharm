from collections import deque

milligrams_coffeine = list(map(int, input().split(", ")))
energy_drinks = deque(list(map(int, input().split(", "))))
stamat_limit = 0


while milligrams_coffeine and energy_drinks:
    current_coffeine = milligrams_coffeine.pop()
    current_energy = energy_drinks.popleft()

    current_sum = current_energy * current_coffeine
    if current_sum <= 300 - stamat_limit:
        stamat_limit += current_sum
    else:
        energy_drinks.append(current_energy)
        stamat_limit -= 30
        if stamat_limit < 0:
            stamat_limit = 0

if energy_drinks:
    result = ", ".join(map(str, energy_drinks))
    print(f'Drinks left: {result}')
elif not energy_drinks:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {stamat_limit} mg caffeine.')
