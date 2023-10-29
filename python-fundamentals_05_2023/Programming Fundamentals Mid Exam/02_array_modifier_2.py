def swap(lst, ind_one, ind_two):
    lst[ind_one], lst[ind_two] = lst[ind_two], lst[ind_one]

def multiply(lst, ind_one, ind_two):
    lst[ind_one] *= lst[ind_two]

def decrease(lst):
    return [num - 1 for num in lst]

lst = [int(x) for x in input().split()]


while True:
    command = input().split()

    if command[0] == 'end':
        break

    if command[0] == 'swap':
        ind_one = int(command[1])
        ind_two = int(command[2])
        # ind_one, ind_two = map(int, command[1:])
        swap(lst, ind_one, ind_two)
    elif command[0] == 'multiply':
        ind_one = int(command[1])
        ind_two = int(command[2])
        # ind_one, ind_two = map(int, command[1:])
        multiply(lst, ind_one, ind_two)
    elif command[0] == 'decrease':
        lst = decrease(lst)

print(*lst, sep=', ')