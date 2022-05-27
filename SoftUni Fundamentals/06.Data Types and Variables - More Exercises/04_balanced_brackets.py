n = int(input())
balanced = 0
for i in range(n):
    string = input()
    if string == "(":
        balanced += 1
        if balanced > 1:
            print("UNBALANCED")
            exit()
    elif string == ")":
        balanced -= 1
if balanced == 0:
    print("BALANCED")
else:
    print("UNBALANCED")


# lines = int(input())
#
# is_balanced = True
# last_bracket = ''
# for _ in range(0, lines):
#     current = input()
#     if current not in ['(', ')']:
#         continue
#
#     if last_bracket == '' and current == ')' or last_bracket == current:
#         is_balanced = False
#         break
#
#     last_bracket = current
#
# if is_balanced:
#     print('BALANCED')
# else:
#     print('UNBALANCED')
