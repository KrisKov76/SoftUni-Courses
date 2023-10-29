from collections import deque

bowls = deque(int(x) for x in input().split(', '))
customers = deque(int(x) for x in input().split(', '))

while bowls and customers:
    ramen = bowls[-1]  # last ramen
    customer = customers[0]  # first customer

    if ramen == customer:
        bowls.pop()
        customers.popleft()
    elif ramen > customer:
        ramen -= customer
        customers.remove(customer)
        bowls[-1] = ramen
    elif customer > ramen:
        customer -= ramen
        bowls.remove(ramen)
        customers[0] = customer

if not customers:
    print("Great job! You served all the customers.")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")

if bowls:
    print(f"Bowls of ramen left: {', '.join(map(str, bowls))}")

if customers:
    print(f"Customers left: {', '.join(map(str, customers))}")
