n = int(input())

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()

for row in range(n - 1, 0, -1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()


 

# 3. Triangle

# Create a module for printing a triangle. You will receive an integer number which is the size of the triangle.

# Examples

# Input Output

# 3

# 1 1 2 1 2 3 1 2 1

# Input Output

# 4 1 1 2 1 2 3 1 2 3 4 1 2 3 1 2 1