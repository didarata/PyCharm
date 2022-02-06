turns_per_game = int(input())

zero_nine = 0
ten_nineteen = 0
tweny_twenynine = 0
thirty_thirtynine = 0
forty_fifty = 0
invalid_number = 0
score = 0

for i in range(turns_per_game):
    turn = int(input())
    if 0 <= turn <= 9:
        score += turn * 0.20
        zero_nine += 1
    elif 10 <= turn <= 19:
        score += turn * 0.30
        ten_nineteen += 1
    elif 20 <= turn <= 29:
        score += turn * 0.40
        tweny_twenynine += 1
    elif 30 <= turn <= 39:
        score += 50
        thirty_thirtynine += 1
    elif 40 <= turn <= 50:
        score += 100
        forty_fifty += 1
    else:
        score /= 2
        invalid_number += 1



print(f'{score:.2f}')
print(f'From 0 to 9: {(zero_nine / turns_per_game) * 100:.2f}%')
print(f'From 10 to 19: {(ten_nineteen / turns_per_game) * 100:.2f}%')
print(f'From 20 to 29: {(tweny_twenynine / turns_per_game) * 100:.2f}%')
print(f'From 30 to 39: {(thirty_thirtynine / turns_per_game) * 100:.2f}%')
print(f'From 40 to 50: {(forty_fifty / turns_per_game) * 100:.2f}%')
print(f'Invalid numbers: {(invalid_number / turns_per_game) * 100:.2f}%')