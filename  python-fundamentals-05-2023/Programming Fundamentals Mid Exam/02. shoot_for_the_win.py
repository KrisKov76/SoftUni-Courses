# 100.0

lst = [int(x) for x in input().split()]
count = 0

while True:

    command = input()

    if command == 'End':
        break

    index = int(command)

    if index in range (len(lst)):
        target_value = lst[index]
        lst[index] = -1
        count += 1

        for i in range(len(lst)):
            if lst[i] != -1:
                if lst[i] > target_value:
                    lst[i] -= target_value
                else:
                    lst[i] += target_value
    else:
        continue

print("Shot targets: {} ->".format(count), *lst)
