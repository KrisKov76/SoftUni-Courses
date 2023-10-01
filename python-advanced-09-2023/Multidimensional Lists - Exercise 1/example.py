matrix = [[''] * 5]

[print(*x) for x in matrix]  # разпакетиране на матрица

matrix[0][1] = 'd'

[print(*x) for x in matrix]