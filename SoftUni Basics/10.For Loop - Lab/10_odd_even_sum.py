n = int(input())
odd_sum = 0
even_sum = 0

for number in range (0, n + 1, 2):
    value = int(input())
    odd_sum += value

print(odd_sum)