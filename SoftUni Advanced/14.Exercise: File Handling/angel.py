try:
    user_input = list(int(x) for x in input().split())
except:
    print("Input must contain only number divided by single empty space. Ex: 1 2 3 4 5 1 2 3 5 6 1 3 5")

dict = {}
count = 0
total_sum = 0

while len(user_input) != 0:
    el = user_input.pop()
    total_sum += el
    if el not in dict:
        dict[el] = 1
    else:
        dict[el] += 1
    count += 1

print(f"Dictionary: {dict}")

sorted_dict = sorted(dict.items(), key=lambda x:x[0])

for key,value in sorted_dict:
    if value > 1:
        print(f"The number {key} is present {value} time's in the dictionary")
    else:
        print(f"The number {key} is present {value} time in the dictionary")

print(f"Total sum = {total_sum}")
