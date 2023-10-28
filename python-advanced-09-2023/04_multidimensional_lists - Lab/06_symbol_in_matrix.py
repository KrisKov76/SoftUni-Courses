rows = int(input())
matrix = []

for row in range(rows):
    # elements = [el for el in input()]
    elements = list(input())

    matrix.append(elements)
# print(matrix)

symbol = input()
position = None

for row in range(rows):
    if position:
        break
    for col in range(len(matrix[row])):
        if matrix[row][col] == symbol:
            position = (row, col)
            print(position)

if not position:
    print(f"{symbol} does not occur in the matrix")