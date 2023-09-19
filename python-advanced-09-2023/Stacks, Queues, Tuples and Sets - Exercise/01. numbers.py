first_set = set(int(x) for x in input().split())  # директно превръщаме в int през входа
second_set = set(int(x) for x in input().split())  # директно превръщаме в int през входа
num = int(input())

for _ in range(num):
    line = input().split()

    # command = line[0] + " " + line[1]
    command = " ".join(line[:2]) # подсказано, като оптимизация от chat gpt
    numbers = [int(x) for x in line[2:]]

    if command == 'Add First':
        first_set.update(numbers)
    elif command == 'Add Second':
        second_set.update(numbers)
    elif command == 'Remove First':
        first_set.difference_update(numbers)
    elif command == 'Remove Second':
        second_set.difference_update(numbers)
    elif command == 'Check Subset':
        print(first_set > second_set)

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')