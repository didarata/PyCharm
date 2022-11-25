def genrange(start: int, end: int):
    for i in range(start, end+1):
        yield i

# def genrange(start_num, end_num):
#     while start_num <= end_num:
#         yield start_num
#         start_num += 1

print(list(genrange(1, 10)))