number_of_electrons = int(input())
n = 0
lst = []

while True:
    n += 1
    max_num_electrons = 2 * n ** 2

    if max_num_electrons < number_of_electrons:
        lst.append(min(max_num_electrons, number_of_electrons))
        number_of_electrons -= max_num_electrons
    else:
        lst.append(min(max_num_electrons, number_of_electrons))
        break
print(lst)
