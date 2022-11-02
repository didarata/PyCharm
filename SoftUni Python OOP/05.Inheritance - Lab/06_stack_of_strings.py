class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        return self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"

# https://judge.softuni.org/Contests/Practice/Index/1940#5
