dictionary = {}

while True:
    entry = input().split()

    if entry[0] == 'buy':
        break

    product, price, quantity = entry[0], float(entry[1]), int(entry[2])

    if product not in dictionary:
        dictionary[product] = [price, quantity]
    else:
        dictionary[product][0] = price
        dictionary[product][1] += quantity

for key, value in dictionary.items():
    print(f'{key} -> {(value[0] * value[1]):.2f}')
