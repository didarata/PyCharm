number = int(input())
bonus = 0
extra_bonus = 0

if number <= 100:
    bonus += 5
elif number <= 1000:
    bonus = number * 0.2
elif number > 1000:
    bonus = number * 0.1

if (number % 2) == 0:
    extra_bonus += 1
elif number % 10 == 5:
    extra_bonus += 2

final_bonus = bonus + extra_bonus
final_number = number + bonus + extra_bonus

print(final_bonus)
print(final_number)