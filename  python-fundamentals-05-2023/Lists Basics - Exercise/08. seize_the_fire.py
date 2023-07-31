effort = 0
total_fire = 0

items = input().split('#')
water = int(input())
print("Cells:")

for item in items:
    items = item.split(' = ')
    level = items[0]
    level_number = int(items[1])

    if level == "High" and 125 >= level_number >= 81 or \
            level == "Medium" and 80 >= level_number >= 51 or \
            level == "Low" and 50 >= level_number >= 1:
        if water < level_number:
            continue
        water -= level_number
        effort += level_number * 0.25
        total_fire += level_number
        print(f' - {level_number}')

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
