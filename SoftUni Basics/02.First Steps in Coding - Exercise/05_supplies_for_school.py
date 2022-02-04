order_pens = int(input())
order_markers = int(input())
order_cleaning_solution = int(input())
discout = int(input())

final_price_pen = order_pens * 5.80
final_price_markers = order_markers * 7.20
final_price_cleaning = order_cleaning_solution * 1.20

total_price = final_price_pen + final_price_markers + final_price_cleaning
total_discount = total_price * ( discout / 100 )

final_price = total_price - total_discount

print(final_price)
