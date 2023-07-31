# 100.0

quantity_food = float(input()) * 1000
quantity_hay = float(input()) * 1000
quantity_cover = float(input()) * 1000
guineas_weight = float(input()) * 1000

days = 0

while True:

    days += 1

    if days > 31:
        break

    if quantity_food <= 0 or quantity_hay <= 0 or quantity_cover <= 0:
        print("Merry must go to the pet store!")
        break

    elif days == 31:
        print(f"Everything is fine! Puppy is happy! Food: {(quantity_food/1000):.2f}, Hay: {(quantity_hay)/1000:.2f}, Cover: {(quantity_cover)/1000:.2f}.")

    quantity_food -= 300

    if days % 2 == 0:
        quantity_hay -= quantity_food * 0.05

    if days % 3 == 0:
        quantity_cover -= 0.333 * guineas_weight
