rows, cols = [int(x) for x in input().split(", ")]
matrix = []

dict = {}

for _ in range(rows):
    elements = [int(el) for el in input().split(', ')]
    matrix.append(elements)

for row in range(rows):
    for col in range(cols):
        if col not in dict:
           dict[col] = []
        dict[col].append([matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]])


