num = int(input())

for i in range(1, num + 1):
    print("")
    for j in range(i):
       print("*", end="")

for i in range(num - 1, -1, -1):
    print("")
    for j in range(i):
       print("*", end="")