rows = cols = int(input())
matrix = []
position = ()

amount_of_fish = 0
quota = 20

# пълним матрицата
for row in range(rows):
    string = [x for x in input()]  # когато нямаме отстояния и не можем да ползваме split()
    matrix.append(string)

    # намираме координатите на тунела, като тюпъли
    for col in range(cols):
        if matrix[row % rows][col % cols] == 'S':
            position = (row, col)
            matrix[row][col] = "-"

# [print(''.join(row)) for row in matrix]  # разпринтиране на матрицата

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}  # речник за посоките
flag = False

while True:
    # подавани команди - нагоре, надолу, наляво, надясно
    command = input()

    pre_row = position[0] % rows
    pre_col = position[1] % cols

    # условие за приключване на while-цикъла
    if command == 'collect the nets':
        matrix[pre_row][pre_col] = "S"
        break

    # move команди и текуща position - oбхождане на матрицата
    move = directions[command]
    # нова позиция
    row = position[0] + move[0]
    col = position[1] + move[1]
    position = (row, col)

    # Проверка за извън границите и обновяване на позицията
    row %= rows
    col %= cols

    # if условия при обхождането на матрицата
    if matrix[row][col].isdigit():
        amount_of_fish += int(matrix[row][col])
        matrix[row][col] = '-'
    elif matrix[row][col] == 'W':
        flag = True
        amount_of_fish = 0
        break

if flag:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: {[pre_row, pre_col]}")

if amount_of_fish >= quota:
    print(f"Success! You managed to reach the quota!")
elif amount_of_fish < quota and not flag:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - amount_of_fish} tons of fish more.")

if amount_of_fish > 0:
    print(f"Amount of fish caught: {amount_of_fish} tons.")

if not flag:
    [print(''.join(row)) for row in matrix]
