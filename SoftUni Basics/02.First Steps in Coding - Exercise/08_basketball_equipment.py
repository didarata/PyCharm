yearly_tax = int(input())

shoes = yearly_tax - (yearly_tax * 0.40)
cloths = shoes - (shoes * 0.20)
ball = cloths / 4
accessories = ball / 5

final_price = yearly_tax + shoes + cloths + ball + accessories

print(final_price)