from collections import deque

player = deque(input().split(', '))
rows = cols = 6

matrix = []
position = ()
blocked = []

# пълним матрицата
for row in range(rows):
    string = input().split()
    matrix.append(string)

    # намираме координатите на подводницата
    for col in range(cols):
        if matrix[row][col] == 'S':
            position = [row, col]
            matrix[row][col] = '-'

# [print(''.join(row)) for row in matrix] # принтиране на матрицата

# directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}  # речник за посоките

while True:

    # подавани команди - нагоре, надолу, наляво, надясно
    command = eval(input())

    # промяна на позицията
    row, col = command[0], command[1]
    position = (row, col)

    # Проверка за извън границите и обновяване на позицията
    row %= rows
    col %= cols

    if player[0] in blocked:
        blocked.remove(player[0])
        player.rotate()
        continue

    # if условия при обхождането на матрицата
    if matrix[row][col] == 'E':
        print(f"{player[0]} found the Exit and wins the game!")
        break
    if matrix[row][col] == 'T':
        player.rotate()
        print(f"{player[1]} is out of the game! The winner is {player[0]}.")
        break
    if matrix[row][col] == 'W':
        blocked.append(player[0])
        print(f"{player[0]} hits a wall and needs to rest.")

    player.rotate()
