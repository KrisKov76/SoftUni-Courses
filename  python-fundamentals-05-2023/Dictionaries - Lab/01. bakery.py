data = input().split()

# for i in range(0, len(data), 2):
#     product = data[i]
#     quantity = int(data[i + 1])
#     stock[product] = quantity
# print(stock)


stock = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}
print(stock)
