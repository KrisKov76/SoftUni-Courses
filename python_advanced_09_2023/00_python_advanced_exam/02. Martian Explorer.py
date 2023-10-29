from collections import deque


def col_positive(col):
    return col % cols


def row_positive(row):
    return row % rows


rows, cols = 6, 6

matrix = []
deposit = {'Water': 0, 'Metal': 0, "Concrete": 0}

position = ()
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for row in range(rows):
    string = input()
    matrix.append(string.split(' '))

    for col in range(cols):
        if matrix[row][col] == 'E':
            position = [row, col]

command = deque(input().split(', '))

while command:
    move = directions[command[0]]
    row = position[0] + move[0]
    col = position[1] + move[1]

    # Обновяване на позицията и матрицата
    position = (row, col)
    command.popleft()

    # Проверка за извън границите и обновяване на позицията
    row %= rows
    col %= cols

    if matrix[row][col] == 'W':
        print(f"Water deposit found at ({row_positive(row)}, {col_positive(col)})")
        deposit['Water'] += 1
    elif matrix[row][col] == 'M':
        print(f"Metal deposit found at ({row_positive(row)}, {col_positive(col)})")
        deposit['Metal'] += 1
    elif matrix[row][col] == 'C':
        print(f"Concrete deposit found at ({row_positive(row)}, {col_positive(col)})")
        deposit['Concrete'] += 1
    elif matrix[row][col] == 'R':
        print(f"Rover got broken at ({row_positive(row)}, {col_positive(col)})")
        break

if sum(deposit.values()) >= 3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")