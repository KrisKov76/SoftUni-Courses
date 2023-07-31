lst = list(map(int, input().split())) # да го сплитне до int

while True:
    command = input().split()

    if command[0] == 'end':
        break

    if command[0] == 'swap':
        ind_one = int(command[1])
        ind_two = int(command[2])
        lst[ind_one], lst[ind_two] = lst[ind_two], lst[ind_one]
    elif command[0] == 'multiply':
        ind_one = int(command[1])
        ind_two = int(command[2])
        lst[ind_one] *= lst[ind_two]
    elif command[0] == 'decrease':
        lst = [num - 1 for num in lst]

print(*lst, sep=', ')