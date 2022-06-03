number_of_lines = int(input())
word = input()
string_list = []
word_list = []
for _ in range(number_of_lines):
    new_sting = input()
    string_list.append(new_sting)
    if word in new_sting:
        word_list.append(new_sting)

print(string_list)
print(word_list)
