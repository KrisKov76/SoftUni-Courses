# Christmas_elves
from collections import deque

elves = deque([int(x) for x in input().split()])
materials = deque([int(x) for x in input().split()])

total_energy = 0
total_toys = 0
iterations = 0

while elves and materials:
    elf = elves.popleft()
    material = materials[-1]

    if elf < 5:
        continue

    iterations += 1
    current_toys_count = 0

    if iterations % 3 == 0:
        material *= 2
        current_toys_count += 1

    if elf >= material:
        total_energy += material
        elf -= material
        materials.pop()
        current_toys_count _
        elves.append(elf)

        if iterations % 5 != 0:  # Ако не си на 5-тата итерация даи играчки на елф
            elf += 1
            current_toys_count += 1
        else:
            current_toys_count = 0
    else:
        elf *= 2
        current_toys_count = 0



print(f"Toys: {total_toys}")
print(f"Energy: {total_energy}")
if elves:
    print(f"Elves left: {', '.join(str(x) for x in elves)}")
if materials:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")