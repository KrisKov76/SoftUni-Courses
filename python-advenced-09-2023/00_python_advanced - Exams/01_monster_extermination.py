from collections import deque

monsters_que = deque(int(x) for x in input().split(',')) # deque - взимаме стойностите отзад напред, оптимизация - O(1)
soldier_stack = [int(x) for x in input().split(',')] # stack - теглим първата стойност, няма значение вече какво е, list или друго
counter = 0

while monsters_que and soldier_stack:
    current_armour = monsters_que.popleft()
    current_strike = soldier_stack.pop()

    if current_strike >= current_armour:
        counter += 1
        current_strike -= current_armour

        if soldier_stack:
            soldier_stack[-1] += current_strike
        elif not soldier_stack and current_strike > 0:
            soldier_stack.append(current_strike)
    else:
        current_armour -= current_strike
        monsters_que.append(current_armour)

if not monsters_que:
    print("All monsters have been killed!")
if not soldier_stack:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {counter}")