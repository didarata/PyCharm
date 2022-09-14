from collections import deque

parentheses = deque(input())
open_per = deque()
balanced = True
while parentheses:
    check_par = parentheses.popleft()
    if check_par in "{[(":
        open_per.append(check_par)
    elif not open_per:
        balanced = False
        break
    else:
        if f"{open_per.pop() + check_par}" not in "{}()[]":
            balanced = False
            break

if balanced and not open_per:
    print("YES")
else:
    print("NO")

# string = input()
# stack = []
# pairs = {
#     "(": ")",
#     "[": "]",
#     "{": "}"
# }
# balanced = True
#
# for ch in string:
#
#     if ch in "([{":
#         stack.append(ch)
#
#     else:
#         if not stack:
#             balanced = False
#
#         else:
#             opening_bracket = stack.pop()
#
#             if pairs[opening_bracket] != ch:
#                 balanced = False
#
#     if not balanced:
#         break
#
# if not balanced or stack:
#     print("NO")
#
# else:
#     print("YES")