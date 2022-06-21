numbers = list(map(int, input().split()))
average = int(sum(numbers) / len(numbers))
above_average = []
for number in numbers:
    if number > average:
        above_average.append(number)

if above_average ==  []:
    print('No')
    exit()
above_average.sort()
above_average.reverse()
above_average = list(map(str, above_average))
output = " ".join(above_average[0:5])
print(output)
