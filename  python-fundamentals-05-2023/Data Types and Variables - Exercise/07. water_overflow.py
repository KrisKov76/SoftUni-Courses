
liters, total_liters = 0, 0

num = int(input())
for i in range(num):
    liters = int(input())
    if total_liters + liters > 255:
        print("Insufficient capacity!")
        continue
    else:
        total_liters += liters
print(total_liters)



