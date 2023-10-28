from collections import deque

monsters = deque(int(x) for x in input().split(','))
soldier = [int(x) for x in input().split(',')]
counter = 0

while monsters and soldier:
    current_armour = monsters.popleft()
    current_strike = soldier.pop()

    if current_strike >= current_armour:
        counter += 1
        current_strike -= current_armour
        if soldier:
            soldier[-1] += current_strike
        elif not soldier and current_strike > 0:
            soldier.append(current_strike)
    else:
        current_armour -= current_strike
        monsters.append(current_armour)

if not monsters:
    print("All monsters have been killed!")
if not soldier:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {counter}")