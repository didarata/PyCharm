part = input()
total_price = []

while part != 'special' and part != 'regular':
    if float(part) >= 0:
        total_price.append(part)
    else:
        print('Invalid price!')
        part = input()
        continue
    part = input()

total_price = [float(i) for i in total_price]
total_price = sum(total_price)
total_tax = total_price * 0.20
total_price_with_tax = total_price + total_tax

if part == "special":
    total_price_with_tax = total_price_with_tax - (total_price_with_tax * 0.10)

if total_price_with_tax == 0:
    print('Invalid order!')
else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price:.2f}$')
    print(f'Taxes: {total_tax:.2f}$')
    print(f'-----------')
    print(f'Total price: {total_price_with_tax:.2f}$')
