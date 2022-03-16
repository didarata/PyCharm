family_member = input()

toys_price = 5
sweater = 15
kids = 0
adults = 0

while family_member != "Christmas":
    family_member = int(family_member)
    if family_member <= 16:
        kids += 1
    else:
        adults += 1
    family_member = input()

print(f'Number of adults: {adults}')
print(f'Number of kids: {kids}')
print(f'Money for toys: {kids * toys_price}')
print(f'Money for sweaters: {adults * sweater}')