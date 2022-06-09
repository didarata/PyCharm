# def repeater(str, count):
#     return str * count
#
#
# str = input()
# count = int(input())
# print(repeater(str, count))

# lambda function
repeater = lambda str, count: str * count


current_string = input()
current_count = int(input())

print(repeater(current_string, current_count))
