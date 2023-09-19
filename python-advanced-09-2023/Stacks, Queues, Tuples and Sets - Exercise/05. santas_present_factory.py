from collections import deque

materials = [int(x) for x in input().split()] # работим с последния елемент
magic = deque(int(x) for x in input().split()) # работим с първия елемент

# правим речник, по-елегантното решение. В това дикшънъри си държим точките от таблицата
points = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}

# правим още един празен речник, в който държим готовите играчки, които още не са направени
presents = {}

while materials and magic:
    total_magic = materials[-1] * magic[0]
    if total_magic in points:
        new_present = points[total_magic]
        if new_present not in presents:
            presents[new_present] = 0
        presents[new_present] += 1
        materials.pop()
        magic.popleft()
    elif  total_magic < 0:
        total_magic = materials[-1] + magic[0]
        materials.append(materials.pop() + magic.popleft())
    elif total_magic > 0:
        magic.popleft()
        materials[-1] += 15
    elif materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()
    elif magic[0] == 0:
        magic.popleft()
    elif materials[-1] == 0:
        materials.pop()

if ('Doll' in presents and 'Wooden train' in presents) or ('Teddy bear' in presents and 'Bicycle' in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials[::-1]])}")

if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for key, value in sorted(presents.items()):
    if value > 0:
        print(f"{key}: {value}")

