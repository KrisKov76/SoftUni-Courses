from collections import deque


def in_boundaries(rw, cl):
    if 0 <= rw < len(matrix) and 0 <= cl < len(matrix[0]):
        return True
    return False


rows = cols = int(input())

matrix = []
position = ()

hazelnuts = 0

command = deque(input().split(', '))

for row in range(rows):
    string = [x for x in input()]  # когато нямаме отстояния и не можем да ползваме split()
    matrix.append(string)

    # намираме координатите
    for col in range(cols):
        if matrix[row][col] == 's':
            position = [row, col]

flag = False

while True:

    # посоки
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

    if len(command) == 0:
        break

    move = directions[command[0]]
    row = position[0] + move[0]
    col = position[1] + move[1]
    position = [row, col]

    command.popleft()  # премахваме [0] посоката от deque

    if not in_boundaries(row, col):
        print("The squirrel is out of the field.")
        flag = True
        break
    if matrix[row][col] == 'h':
        matrix[row][col] = '*'
        hazelnuts += 1
        if hazelnuts == 3:
            flag = True
            print("Good job! You have collected all hazelnuts!")
            break
    elif matrix[row][col] == 't':
        flag = True
        print("Unfortunately, the squirrel stepped on a trap...")

print(f"Hazelnuts collected: {hazelnuts}")

if hazelnuts < 3 and not flag:
    print("There are more hazelnuts to collect.")

# 87/100