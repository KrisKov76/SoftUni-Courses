# matrix = [['*' for _ in range(3)] for _ in range(3)]
# print(matrix)
#
# # заместване на символ в матрицата
# matrix[1][1] = '@'
# print(matrix)
#
# # идеята за rows(дължината на матрицата) и cols(дължината на нулевия стринг на матрицата)
# rows = len(matrix)
# cols = len(matrix[0])
#
# # намиране на кое място в матрицата е звездичката '*'
# for i in range(rows):
#     for j in range(cols):
#         if matrix[i][j] == '*':
#             start_row = i
#             start_col = j
#
# print(f'rows: {rows} \ncols: {cols}')

# matrix = [['*' for _ in range(3)] for _ in range(3)]

matrix = [
    ['*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', ' ', '*'],
    ['*', '*', '*', '@', ' ', '*'],
    ['*', '*', '*', '*', ' ', ' '],
    ['*', '*', ' ', ' ', '*', ' '],
    ['*', '*', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', '*', '*', '*'],
    [' ', '*', '*', '*', '*', '*'],
    [' ', '*', '*', '*', '*', '*'],
]

print(matrix)

i = 0

# принтиране на матрицата с редове един под друг:
for row in matrix:
    print(' '.join(row))

# # rows = len(matrix)
# cols = len(matrix[0])
#
# for i in range(rows):
#     for j in range(cols):
#         if matrix[i][j] == '@':
#             curr_row = i
#             curr_col = j

# curr_row = 2
# curr_col = 3
#
#
# while i < 13:
#     i += 1
#
#     # left
#     if matrix[curr_row][curr_col - i] == ' ' and matrix[curr_row][curr_col] == '@':
#         curr_col = curr_col - i
#         matrix[curr_row][curr_col] = '@'
#         matrix[curr_row][curr_col + 1] = '.'
#     # down
#     elif matrix[curr_row + i][curr_col] == ' ' and matrix[curr_row][curr_col] == '@':
#         curr_row = curr_row + i
#         matrix[curr_row][curr_col] = '@'
#         matrix[curr_row - i][curr_col] = '.'
#     # right
#     elif matrix[curr_row][curr_col + i] == ' ' and matrix[curr_row][curr_col] == '@':
#         curr_col = curr_col + i
#         matrix[curr_row][curr_col] = '@'
#         matrix[curr_row][curr_col - 1] = '.'
#     # up
#     elif matrix[curr_row - i][curr_col] == ' ' and matrix[curr_row][curr_col] == '@':
#         curr_row = curr_row - i
#         matrix[curr_row][curr_col] = '@'
#         matrix[curr_row + i][curr_col] = '.'
#
#
#
#     for row in matrix:
#         print(' '.join(row))
#     print('                   ')
#
#     i = 0
