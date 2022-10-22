from email.mime import base
from math import log, e

number = int(input())
base_input = input()
# -------------------------------
# base = e if base_input == 'natural' else int(base_input)
# print(log(number, base))
# -------------------------------
# if base_input == 'natural':
#     print(log(number))
# else:
#     print(log(number, (int(base_input))))
# -------------------------------

result = log(number) if base_input == 'natural' else log(number, int(base_input))
print(result)



# 1. Calculate Logarithm

# Write a program that prints the calculated logarithm of any given number

# Input

# · On the first line, you will receive the number (an integer)

# · On the second line, you will receive a number, which is the logarithm base. It can be either a number or the word "natural"

# The output should be formatted to the 2nd decimal digit


# Examples

# Input Output

# 10

# natural 2.30

# Input Output

# 10

# 10 1.00