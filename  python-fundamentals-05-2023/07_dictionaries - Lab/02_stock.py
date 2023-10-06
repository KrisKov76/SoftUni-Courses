data = input().split()

# създаваме си речника stock
stock = {}

for i in range(0, len(data), 2):
    product = data[i]
    quantity = int(data[i + 1])
    stock[product] = quantity

# създаваме си списък с търсените продукти
products_to_search = input().split()

# обхождаме списъка с продукти
for product in products_to_search:
    # търсим дали продукт от търсените съответства на продукти(ключове) в речника
    if product in stock:
        print(f'We have {stock[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")
