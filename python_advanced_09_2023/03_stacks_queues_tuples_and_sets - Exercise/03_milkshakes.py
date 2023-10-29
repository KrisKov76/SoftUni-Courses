from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milk = deque(int(x) for x in input().split(', '))
milkshakes = 0

while chocolates and milk and milkshakes < 5:
    if chocolates[-1] <= 0 and milk[0] <= 0:
        chocolates.pop()
        milk.popleft()
        continue

    if chocolates[-1] <= 0:
        chocolates.pop()
        continue

    if milk[0] <= 0:
        milk.popleft()
        continue

    if chocolates[-1] == milk[0]:
        chocolates.pop()
        milk.popleft()
        milkshakes += 1
    else:
        milk.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join([str(x) for x in chocolates]) if chocolates else 'empty'}")
print(f"Milk: {', '.join([str(x) for x in milk]) if milk else 'empty'}")