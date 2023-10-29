
fights = int(input())

helmet, sword, shield, armor = float(input()), float(input()), float(input()), float(input())

i2 = 0
expences = 0

for i in range(1, fights + 1):
    if i % 2 == 0:
        expences += helmet
    if i % 3 == 0:
        expences += sword
    if i % 2 == 0 and i % 3 == 0:
        expences += shield
        i2 += 1
        if i2 % 2 == 0:
            expences += armor

print(f"Gladiator expenses: {expences:.2f} aureus")

