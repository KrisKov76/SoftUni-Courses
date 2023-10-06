from math import floor

person = int(input())
days = int(input())
coins = 0

for i in range(1, days + 1):

    if i % 10 == 0:
        person -= 2
    if i % 15 == 0:
        person += 5

    if i % 3 == 0:
        coins -= 3 * person
    if i % 5 == 0:
        coins += 20 * person
        if i % 3 == 0:
            coins -= 2 * person

    coins += 50
    coins -= 2 * person
    total_coins = coins / person

print(f"{person} companions received {floor(total_coins)} coins each.")

# кратно на 2 - i % 2 == 0
# кратно на 7  - i % 7 == 0