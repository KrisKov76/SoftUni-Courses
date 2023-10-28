from collections import deque

caffeine = deque(int(x) for x in input().split(', '))
energy_drink = deque(int(x) for x in input().split(', '))
total_drank = 0

while caffeine and energy_drink:
    caffeine_ = caffeine.pop()
    energy_ = energy_drink.popleft()

    result = caffeine_ * energy_

    if result + total_drank <= 300:
        total_drank += result
    else:
        energy_drink.append(energy_)
        if total_drank > 0:
            total_drank -= 30

if energy_drink:
    energy_str = ', '.join(map(str, energy_drink))
    print(f"Drinks left: {energy_str}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_drank} mg caffeine.")


