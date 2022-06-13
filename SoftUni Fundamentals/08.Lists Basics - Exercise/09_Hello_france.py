# collection_of_items = input().split("|")
# budget = int(input())
# train_ticket = 150
# total_money = 0
# items_bought = []
# profit = 0
# for index in collection_of_items:
#     current_item_list = index.split('->')
#     current_item = current_item_list[0]
#     current_price = float(current_item_list[1])
#     while budget >= current_price:
#         if current_item == 'Clothes' and current_price <= 50.00:
#             profit += current_price * 0.40
#             total_money += current_price + profit
#             budget -= current_price
#             items_bought.append(current_price + (current_price * 0.40))
#             break
#         elif current_item == 'Shoes' and current_price <= 35.00:
#             profit += current_price * 0.40
#             total_money += current_price + profit
#             budget -= current_price
#             items_bought.append(current_price + (current_price * 0.40))
#             break
#         elif current_item == 'Accessories' and current_price <= 20.50:
#             profit += current_price * 0.40
#             total_money += current_price + profit
#             budget -= current_price
#             items_bought.append(current_price + (current_price * 0.40))
#             break
#         break
#
# formatted_item_bought = ['%.2f' % elem for elem in items_bought]
# print(*formatted_item_bought, sep=" ")
# print(f'Profit: {profit:.2f}')
# if total_money >= train_ticket:
#     print('Hello, France!')
# else:
#     print('Not enough money.')


collection_of_items = input().split("|")
budget = int(input())
train_ticket = 150
total_money = 0
items_bought = []
budget_left = budget
for index in collection_of_items:
    current_item_list = index.split('->')
    current_item = current_item_list[0]
    current_price = float(current_item_list[1])
    if budget_left >= current_price:
        if current_item == 'Clothes' and current_price <= 50.00:
            total_money += current_price
            budget_left -= current_price
            items_bought.append(current_price + (current_price * 0.40))
        elif current_item == 'Shoes' and current_price <= 35.00:
            total_money += current_price
            budget_left -= current_price
            items_bought.append(current_price + (current_price * 0.40))
        elif current_item == 'Accessories' and current_price <= 20.50:
            total_money += current_price
            budget_left -= current_price
            items_bought.append(current_price + (current_price * 0.40))

difference = sum(items_bought) - total_money
print(' '.join(f'{n:.2f}' for n in items_bought))
print(f'Profit: {difference:.2f}')
if budget + difference > train_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')
