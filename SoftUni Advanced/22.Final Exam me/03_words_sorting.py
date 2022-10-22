def words_sorting(*words):
    word_dict = {}
    result = []

    for word in words:
        for letter in word:
            if word not in word_dict:
                word_dict[word] = ord(letter)
            else:
                word_dict[word] += ord(letter)
    total_value = 0
    for key, value in word_dict.items():
        total_value += value

    if total_value % 2 == 0:
        world_dict_sorted = sorted(word_dict.items(), key=lambda x: x[0])
    else:
        world_dict_sorted = sorted(word_dict.items(), key=lambda x: x[1], reverse = True)

    for key, value in world_dict_sorted:
        result.append(f"{key} - {value}")

    return "\n".join(result)


# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#     ))

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#     ))

print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
