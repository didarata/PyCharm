numbers = list(map(int, input().split(", ")))
current_list = []
boundary = 0
while len(numbers) > 0:
    boundary += 1
    for el in numbers:
        if int(el) <= boundary * 10:
            current_list.append(el)
    print(f"Group of {boundary}0's: {current_list}")
    for copy in current_list:
        if copy in numbers:
            numbers.remove(copy)
    current_list.clear()
