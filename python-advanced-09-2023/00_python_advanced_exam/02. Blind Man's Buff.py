def in_boundaries(rw, cl):
    if 0 <= rw < len(matrix) and 0 <= cl < len(matrix[0]):
        return True
    return False


rows, cols = [int(x) for x in input().split()]

matrix = []
position = ()

# touched opponents and moves
touched_opponents = 0
moves = 0

# пълним матрицата
for row in range(rows):
    string = input().split()
    matrix.append(string)

    # намираме началните координати
    for col in range(cols):
        if matrix[row][col] == 'B':
            position = [row, col]
            matrix[row][col] = '-'

# [print(' '.join(row)) for row in matrix]  # принтиране на матрицата
# print()

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}  # речник за посоките

while True:
    if touched_opponents == 3:
        break
    # подавани команди - нагоре, надолу, наляво, надясно
    command = input()

    if command == 'Finish':
        break

    # move команди и текуща position - oбхождане на матрицата
    move = directions[command]

    # промяна на позицията
    row = position[0] + move[0]
    col = position[1] + move[1]

    # кога не дава право на ход - извън границите на матрицата или когато е на obstacles
    if not in_boundaries(row, col) or matrix[row][col] == 'O':
        continue
    else:
        position = [row, col]

    # if условия при обхождането на матрицата
    if matrix[row][col] == 'P':  # opponents
        touched_opponents += 1
        moves += 1
        matrix[row][col] = '-'
    elif matrix[row][col] == '-':
        moves += 1

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves}")
