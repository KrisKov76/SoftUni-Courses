matrix = []

# rows = 6, cols = 6 - по условие
rows, cols = 6, 6

position = ()  # винаги си генерираме позицията
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

# пълним матрицата
for row in range(rows):
    string = input()
    matrix.append(string.split(' '))

# четем first position
tup = input()
r, c = int(tup[1]), int(tup[4])
position = [r, c]

while True:
    # четем пакета команди
    command = input().split(', ')

    # Stop - условие за край на while цикъла
    if command[0] == 'Stop':
        break

    # move команди и текуща position
    move = directions[command[1]]
    row = position[0] + move[0]
    col = position[1] + move[1]
    position = [row, col]

    # текущи команди - Create, Update, Delete, Read
    if command[0] == 'Create':
        if matrix[row][col] == '.':
            matrix[row][col] = command[2]
    elif command[0] == 'Update':
        if matrix[row][col] != '.':
            matrix[row][col] = command[2]
    elif command[0] == 'Delete':
        if matrix[row][col] != '.':
            matrix[row][col] = '.'
    elif command[0] == 'Read':
        if matrix[row][col] != '.':
            print(matrix[row][col])

[print(' '.join(row)) for row in matrix]
