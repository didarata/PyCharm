from collections import deque

bowls_of_ramen = deque([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])




while bowls_of_ramen and customers:
    ramen = bowls_of_ramen.pop()
    customer = customers.popleft()

    if ramen == customer:
        continue
    if ramen > customer:
        ramen -= customer
        bowls_of_ramen.append(ramen)
        continue
    if ramen < customer:
        customer -= ramen
        customers.appendleft(customer)
        continue

bowls_of_ramen_list = ", ".join(map(str, bowls_of_ramen))
customers_list = ", ".join(map(str, customers))

if customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {customers_list}")
else:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {bowls_of_ramen_list}")