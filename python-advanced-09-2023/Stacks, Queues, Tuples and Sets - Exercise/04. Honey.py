from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbol = deque(input().split())

total_honey = []

while bees and nectar:
    first_bee = bees[0]
    last_nectar = nectar[-1]

    if last_nectar >= first_bee:
        if symbol[0] == '+':
            total_honey.append(abs(first_bee + last_nectar))
        if symbol[0] == '-':
            total_honey.append(abs(first_bee - last_nectar))
        if symbol[0] == '*':
            total_honey.append(abs(first_bee * last_nectar))
        if symbol[0] == '/':
            if last_nectar == 0:
                bees.popleft()
                nectar.pop()
                symbol.popleft()
                continue
            else:
                total_honey.append(abs(first_bee / last_nectar))
        bees.popleft()
        nectar.pop()
        symbol.popleft()
    else:
        nectar.pop()
        continue

print(f"Total honey made: {sum(total_honey)}")

if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")

if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
