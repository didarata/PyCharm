deposite = float(input())
periot = float(input())
yearly_percentage = float(input())
montly_percentage = ((deposite * yearly_percentage) / 100) / 12

print(deposite + (periot * montly_percentage))