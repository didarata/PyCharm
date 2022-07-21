sequence_of_strings = input().split()
results = []

for sequence in sequence_of_strings:
    if len(sequence) != 0:
        current_number = sequence[1:-1]
        first_letter = sequence[0]
        second_letter = sequence[-1]
        first_result = 0
        if first_letter.isupper():
            first_result = int(current_number) / (ord(first_letter) - 64)
        elif first_letter.islower():
            first_result = int(current_number) * (ord(first_letter) - 96)
        second_result = 0
        if second_letter.isupper():
            second_result = first_result - (ord(second_letter) - 64)
        elif second_letter.islower():
            second_result = first_result + (ord(second_letter) - 96)
        results.append(second_result)

print(f'{sum(results):.2f}')
