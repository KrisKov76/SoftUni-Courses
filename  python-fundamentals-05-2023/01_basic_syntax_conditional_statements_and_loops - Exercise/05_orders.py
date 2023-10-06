number_of_orders = int(input())
total_price = 0

for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    number_of_capsules = int(input())

    price = price_per_capsule * number_of_capsules * days

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= number_of_capsules <= 2000:
        print(f"The price for the coffee is: ${price:.2f}")
        total_price += price

print(f"Total: ${total_price:.2f}")
