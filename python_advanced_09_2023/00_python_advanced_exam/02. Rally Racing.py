rows = cols = int(input())
racing_number = input()

matrix = []
tunnel = []
distance_covered = 0

# пълним матрицата
for row in range(rows):
    string = input()
    matrix.append(string.split(' '))

    # намираме координатите на тунела, като тюпъли
    for col in range(cols):
        if matrix[row][col] == 'T':
            tunnel.append((row, col))

# [print(''.join(row)) for row in matrix] # разпринтиране на матрицата

position = (0, 0)  # начална позиция
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}  # речник за посоките

while True:
    # подавани команди - нагоре, надолу, наляво, надясно
    command = input()

    # условие за приключване на while-цикъла
    if command == 'End':
        matrix[position[0]][position[1]] = 'C'
        print(f"Racing car {racing_number} DNF.")
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
    if matrix[row][col] == '.':
        distance_covered += 10
    if matrix[row][col] == 'T':
        distance_covered += 30
        matrix[row][col] = '.'
        tunnel.remove(position)
        position = tunnel[0]
        matrix[position[0]][position[1]] = '.'
    if matrix[row][col] == 'F':
        distance_covered += 10
        matrix[row][col] = 'C'
        print(f"Racing car {racing_number} finished the stage!")
        break

print(f"Distance covered {distance_covered} km.")
[print(''.join(row)) for row in matrix]  # принтиране на матрицата
