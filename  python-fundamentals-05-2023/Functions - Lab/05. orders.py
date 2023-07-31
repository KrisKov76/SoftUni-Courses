def order(name_of_product):
    if name_of_product == "coffee":
        return 1.50
    elif name_of_product == "water":
        return 1.00
    elif name_of_product == "coke":
        return 1.40
    elif name_of_product == "snacks":
        return 2.00

product = input()
num = float(input())

total_sum = order(product) * num
print(f"{total_sum:.2f}")

