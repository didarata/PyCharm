circle = input().split(' ')
kill_count = int(input())
result = []
counter = 0
index = 0

while len(circle) > 0:
    counter += 1

    if counter % kill_count == 0:
        result.append(circle.pop(index))
    else:
        index += 1

    if index >= len(circle):
        index = 0

print(str(result).replace(' ', '').replace('\'', ''))

# ----------------------------------------------------------------------------------
#
# def josephus(elements, skip):
#     idx = 0
#     result = []
#     while len(elements) > 0:
#         idx = (idx + skip - 1) % len(elements)
#         result.append((elements.pop(idx)))
#
#     return result
#
#
# def trim_white_spaces(elements):
#     return '[' + ','.join(elements) + ']'
#
#
# elements_list = input().split()
# k = int(input())
#
# print((trim_white_spaces(josephus(elements_list, k))))
