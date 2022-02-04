#Giraffe Language
#vowels -> g
#---------------

#dog -> dgg
#cat -> cgt

def translate(phrase):
    tranlateion = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                tranlateion = tranlateion + "G"
            else:
                tranlateion = tranlateion + "g"
        else:
            tranlateion = tranlateion + letter
    return  tranlateion

print(translate(input("Enter a Phrase: ")))