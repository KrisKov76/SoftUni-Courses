budget = float(input())
number_of_loaves = 0
colored_eggs = 0

price_flour = float(input())
price_eggs = price_flour * 0.75
price_milk = price_flour * 1.25

price_easter_bread = price_milk * 0.25 + price_eggs + price_flour

while True:

    if budget < price_easter_bread:
        break

    budget -= price_easter_bread
    number_of_loaves += 1
    colored_eggs += 3

    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")




