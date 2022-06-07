factor = int(input())
count = int(input())
final_list = []
random = 0
for number in range(count):
    final_list.append(random + factor)
    random += factor

print(final_list)
