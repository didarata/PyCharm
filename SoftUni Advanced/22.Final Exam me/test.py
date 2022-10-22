arr = [1,2, 2, 3, 4, 2, 7, 8, 8, 3]
same_symbols = []

while arr:
    current_number = arr.pop()
    if current_number in arr:
        if current_number not in same_symbols:
            same_symbols.append(current_number)

print(same_symbols)
