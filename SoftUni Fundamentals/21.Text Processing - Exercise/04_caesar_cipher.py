text = input()

encrypted_version = ""

for symbol in text:
    char = ord(symbol) + 3
    encrypted_version += chr(char)

print(encrypted_version)
