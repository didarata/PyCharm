juniors_cyclist = int(input())
seniors_cyclist = int(input())
type_of_road = input()

tax_junior = 0
tax_senior = 0

if type_of_road == 'trail':
   tax_junior = 5.50
   tax_senior = 7
elif type_of_road == 'downhill':
    tax_junior = 12.25
    tax_senior = 13.75
elif type_of_road == 'road':
    tax_junior = 20
    tax_senior = 21.50
elif type_of_road == 'cross-country':
    tax_junior = 8
    tax_senior = 9.50

tax = (juniors_cyclist * tax_junior) + (seniors_cyclist * tax_senior)
tax_with_discount =  tax - (tax * 0.05)

if type_of_road == 'cross-country' and (juniors_cyclist + seniors_cyclist) >= 50:
    tax_with_discount -= tax_with_discount * 0.25

print(f'{tax_with_discount:.2f}')