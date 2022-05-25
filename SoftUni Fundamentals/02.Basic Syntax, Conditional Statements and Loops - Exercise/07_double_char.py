string_name = input()

while string_name != "End":
    double_string = ''
    if string_name == "SoftUni":
        string_name = input()
        continue
    else:
        for letter in string_name:
            double_string += letter * 2
    print(double_string)
    string_name = input()
