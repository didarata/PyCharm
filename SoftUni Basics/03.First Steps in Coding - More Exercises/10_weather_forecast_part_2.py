celsius = float(input())

if 26.00 <= celsius <= 35.00:
    print('Hot')
elif 20.1 <= celsius <= 25.9:
    print('Warm')
elif 15.00 <= celsius <= 20.00:
    print('Mild')
elif 12.00 <= celsius <= 14.9:
    print('Cool')
elif 5.00 <= celsius <= 11.9:
    print('Cold')
else:
    print('unknown')