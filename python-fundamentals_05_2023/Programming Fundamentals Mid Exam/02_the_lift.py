MAX_SIZE = 4

people = int(input())
lift = [int(x) for x in input().split()] # въвеждане на числа в списък

for i in range(len(lift)):
    free_sizes = MAX_SIZE - lift[i]

    lift[i] = min(MAX_SIZE, people + lift[i])
    people -= free_sizes

    if people <= 0:
        break

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*lift)
elif people == 0 and min(lift) == MAX_SIZE:
    print(*lift)
else:
    print("The lift has empty spots!")
    print(*lift)
