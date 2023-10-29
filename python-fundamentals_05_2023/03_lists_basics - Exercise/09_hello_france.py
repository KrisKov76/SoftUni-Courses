item_price = input().split('|')
budget = float(input())

prices = []
profit = 0

for item in item_price:
    items = item.split('->')
    type_items = items[0]
    buying_price = float(items[1])

    if (type_items == "Clothes" and buying_price <= 50) or \
            (type_items == "Shoes" and buying_price <= 35) or \
            (type_items == "Accessories" and buying_price <= 20.50):
        if budget < buying_price:
            continue
        else:
            budget -= buying_price
            selling_price = round(buying_price * 1.4, 2)
            prices.append(selling_price)
            profit += selling_price - buying_price

for price in prices:
    print(f'{price:.2f}', end=' ')
print(f"\nProfit: {profit:.2f}")

if budget + sum(prices) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
