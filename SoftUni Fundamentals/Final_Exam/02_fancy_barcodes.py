import re

pattern = r"@\#{1,}([A-Z][A-Za-z0-9]{4,}[A-Z])@\#{1,}"
number_of_barcodes = int(input())
current_group = ""
for _ in range(number_of_barcodes):
    barcode = input()

    if re.match(pattern, barcode):
        for digit in barcode:
            if digit.isdigit():
                current_group += digit
        if current_group == "":
            print("Product group: 00")
        else:
            print(f"Product group: {current_group}")
        current_group = ""
    else:
        print("Invalid barcode")
