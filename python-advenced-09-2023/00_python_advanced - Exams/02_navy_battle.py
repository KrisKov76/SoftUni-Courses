rows = cols = int(input())
matrix = []
position = ()

counter_mines = 0
counter_cruiser = 0

# пълним матрицата
for row in range(rows):
    string = [x for x in input()]  # когато нямаме отстояния и не можем да ползваме split()
    matrix.append(string)

    # намираме координатите на подводницата
    for col in range(cols):
        if matrix[row][col] == 'S':
            position = [row, col]
            matrix[row][col] = '-'

# [print(''.join(row)) for row in matrix] # разпринтиране на матрицата

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}  # речник за посоките

while True:
    # подавани команди - нагоре, надолу, наляво, надясно
    command = input()

    # move команди и текуща position - oбхождане на матрицата
    move = directions[command]

    # промяна на позицията
    row = position[0] + move[0]
    col = position[1] + move[1]
    position = (row, col)

    # Проверка за извън границите и обновяване на позицията
    row %= rows
    col %= cols

    # if условия при обхождането на матрицата
    if matrix[row][col] == '*':
        matrix[row][col] = '-'
        counter_mines += 1
        if counter_mines == 3:
            matrix[row][col] = 'S'
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
            break
    if matrix[row][col] == 'C':
        counter_cruiser += 1
        matrix[row][col] = '-'
        if counter_cruiser == 3:
            matrix[row][col] = 'S'
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

[print(''.join(row)) for row in matrix]  # разпринтиране на матрицата
