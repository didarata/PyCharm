words = input().split()
filtered_words = [words for words in words if len(words) % 2 == 0]
print('\n'.join(filtered_words))
