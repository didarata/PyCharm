phrase = "Giraffe Academy"
print(phrase.lower())     # .lower makes everything lower case.
print(phrase.upper())     # .upper makes everything upper case.
print(phrase.isupper())     # .isupper checks if entire string is upper case.
print(phrase.upper().isupper())   # you can use those functions in combinations.
print(len(phrase))      # len is function for finding the length of the character inside the string
print(phrase[0])       # [] gives you the character you need, count starts from 0, so first character is 0, 2nd is 1 and so on.
print(phrase.index("a"))       # index function, tells us where specific character or string is located inside of our string.
print(phrase.replace("Giraffe", "Elephant"))     # replace strings and integers inside our strings

phrase = "Giraffe Academy"
print(phrase + " is cool.")      # I think printing variable with text in the same line is called CONCATENATION.
print("Giraffe\"Academy")       # \n print on new line, \ escape character so \" would work, using just \ is just \