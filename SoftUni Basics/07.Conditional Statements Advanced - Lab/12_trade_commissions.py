city = input()
sales = float(input())

commision = 0

if 0 <= sales <= 500:
    if city == 'Sofia':
        commision = sales * 0.05
    elif city == 'Varna':
        commision = sales * 0.045
    elif city == 'Plovdiv':
        commision = sales * 0.055

if 500 < sales <= 1000:
    if city == 'Sofia':
        commision = sales * 0.07
    elif city == 'Varna':
        commision = sales * 0.075
    elif city == 'Plovdiv':
        commision = sales * 0.08

if 1000 < sales <= 10000:
    if city == 'Sofia':
        commision = sales * 0.08
    elif city == 'Varna':
        commision = sales * 0.10
    elif city == 'Plovdiv':
        commision = sales * 0.12

if sales > 10000:
    if city == 'Sofia':
        commision = sales * 0.12
    elif city == 'Varna':
        commision = sales * 0.13
    elif city == 'Plovdiv':
        commision = sales * 0.145


if commision == 0:
    print("error")
else:
    print(f'{commision:.2f}')