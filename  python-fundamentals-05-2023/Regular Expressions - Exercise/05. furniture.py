import re

bought_furniture = []
total_money = 0

while True:
    command = input()

    if command == 'Purchase':
        break

    pattern = r'>>([A-Za-z]+)<<(\d+\.?\d+)!([\d]+)'
    match = re.search(pattern, command)

    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_money += float(price) * int(quantity)

print('Bought furniture:')
for furniture in bought_furniture:
    print(furniture)
print(f'Total money spend: {total_money:.2f}')
