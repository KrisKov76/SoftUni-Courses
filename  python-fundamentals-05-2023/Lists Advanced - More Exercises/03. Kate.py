# row = int(input())
# lst = [input() for x in range(row)]
# matrix = [list(row) for row in lst]
#
# curr_row = 0
# curr_col = 0
# count = 0
# total_count = 0
#
# rows = len(matrix)
# cols = len(matrix[0])
#
# # намира current позицията на символа 'k'
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j] == 'k':
#             curr_row = i
#             curr_col = j
#
# is_True = False
#
# while True:
#     count += 1
#
#     if curr_row == 0 or curr_row + 1 == len(matrix) or curr_col + 1 == len(matrix[0]) or curr_col == 0:
#         print(f'Kate got out in {total_count + 1} moves')
#         break
#
#     if is_True:
#         print("Kate cannot get out")
#         break
#
#         # left
#     if matrix[curr_row][curr_col - 1] == ' ' and matrix[curr_row][curr_col] == 'k':
#         curr_col = curr_col - 1
#         matrix[curr_row][curr_col] = 'k'
#         matrix[curr_row][curr_col + 1] = '.'
#         is_True = False
#     # down
#     elif matrix[curr_row + 1][curr_col] == ' ' and matrix[curr_row][curr_col] == 'k':
#         curr_row = curr_row + 1
#         matrix[curr_row][curr_col] = 'k'
#         matrix[curr_row - 1][curr_col] = '.'
#         is_True = False
#     # right
#     elif matrix[curr_row][curr_col + 1] == ' ' and matrix[curr_row][curr_col] == 'k':
#         curr_col = curr_col + 1
#         matrix[curr_row][curr_col] = 'k'
#         matrix[curr_row][curr_col - 1] = '.'
#         is_True = False
#     # up
#     elif matrix[curr_row - 1][curr_col] == ' ' and matrix[curr_row][curr_col] == 'k':
#         curr_row = curr_row - 1
#         matrix[curr_row][curr_col] = 'k'
#         matrix[curr_row + 1][curr_col] = '.'
#         is_True = False
#     else:
#         is_True = True
#
#     # принтира матрицата
#     for row in matrix:
#         print(' '.join(row))
#     print('')
#
#     total_count += count
#     count = 0


# 100.0

def find_way_out(r, c, moves):
    if not (0 <= r < len(matrix) and 0 <= c < len(matrix[0])):
        return moves

    if matrix[r][c] == "#":
        return 0

    matrix[r][c] = "#"

    result1 = find_way_out(r + 1, c, moves + 1)
    result2 = find_way_out(r - 1, c, moves + 1)
    result3 = find_way_out(r, c + 1, moves + 1)
    result4 = find_way_out(r, c - 1, moves + 1)

    print(f'right: {result1}, left: {result2}, down: {result3}, up: {result4})')

    return max(result1, result2, result3, result4)

# Въвеждаме входни данни
matrix = []
kate_pos = []

for row in range(int(input())):
    matrix.append(list(input()))

    if "k" in matrix[row]:
        kate_pos = [row, matrix[row].index("k")]

for r in matrix:
    print(' '.join(r))

print(kate_pos)


out_in = find_way_out(kate_pos[0], kate_pos[1], 0)

if not out_in:
    print(f"Kate cannot get out")
else:
    print(f"Kate got out in {out_in} moves")
