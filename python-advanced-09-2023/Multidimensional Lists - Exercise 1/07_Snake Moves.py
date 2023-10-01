from collections import deque

r, c = [int(x) for x in input().split()]

string = deque(input())

matrix = []

for row in range(r):
    matrix.append([''] * c) # създаваме празна матрица, която ще пълним
    for col in range(c):
        if row % 2 == 0:
            matrix[row][col] = string[0]
        else:
            matrix[row][-1-col] = string[0]
        string.rotate(-1)


[print(*row, sep='') for row in matrix]