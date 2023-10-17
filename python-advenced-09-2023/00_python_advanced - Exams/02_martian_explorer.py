from collections import deque


def col_positive(col):
    if col >= 0:
        return col
    return len(matrix[0]) + col

def row_positive(row):
    if row >= 0:
        return row
    return len(matrix) + row


rows, cols = 6, 6  # matrix - 6x6
matrix = []
deposit = {'Water': 0, 'Metal': 0, "Concrete": 0}
count = 1

position = ()  # позиция -
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}  # речник за посоките

result = ''

# пълним матрицата
for row in range(rows):
    string = input()
    matrix.append(string.split(' '))

    # намираме първоначалната позииция, отбелязана с 'E'
    for col in range(cols):
        if matrix[row][col] == 'E':
            position = [row, col]

# четем командите
command = deque(input().split(', '))

while command:
    # move команди и текуща position
    move = directions[command[count - 1]]
    # нова позиция
    row = position[0] + move[0]
    col = position[1] + move[1]
    position = (row, col)

    # Проверка за извън границите и обновяване на позицията
    row %= rows
    col %= cols

    if matrix[row][col] == 'W':
        result += f"Water deposit found at ({row_positive(row)}, {col_positive(col)})\n"
        deposit['Water'] += 1
    elif matrix[row][col] == 'M':
        result += f"Metal deposit found at ({row_positive(row)}, {col_positive(col)})\n"
        deposit['Metal'] += 1
    elif matrix[row][col] == 'C':
        result += f"Concrete deposit found at ({row_positive(row)}, {col_positive(col)})\n"
        deposit['Concrete'] += 1
    elif matrix[row][col] == 'R':
        result += f"Rover got broken at ({row_positive(row)}, {col_positive(col)})\n"
        break

    command.popleft()

if sum(deposit.values()) >= 3:
    result += "Area suitable to start the colony."
else:
    result += "Area not suitable to start the colony."
