m = int(input())  # number (count) of presents
n = int(input())  # the size of the neighborhood

matrix = []
santa_position = ()

count_nice_kids = 0
nice_kids = 0

r, c = 0, 0
rw, cl = 0, 0

# пълним матрицата и намираме позицията на човечето - Santa ('S')
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'S':
            santa_position = [row, col]
            matrix[row][col] = '-'  # заместваме веднага символа на S с -
        if matrix[row][col] == 'V':
            count_nice_kids += 1

# възможни позиции при движението на Santa - нагоре, надолу, наляво и надясно
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
circle = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while m > 0:  # условия за прекратяване на цикъла - да свършат подаръците
    command = input()  # четем командите

    if command == 'Christmas morning': # 2-ро условие за прекратяване на цикъла
        break

    move = directions[command]
    row = santa_position[0] + move[0]
    col = santa_position[1] + move[1]
    santa_position = [row, col]

    # кога прекъсваме цикъка - когато излезем извън матрицата или ако попаднем на 'R'
    if row < 0 or row >= n or col < 0 or col >= n:
        break

    if matrix[row][col] == 'V':
        m -= 1
        nice_kids += 1

    # oбхождам всички полета, в 4-те посоки, за да разбера дали има там деца (послушни и непослушни)
    if matrix[row][col] == 'C':
        for i in range(len(circle)):
            rw = circle[i][0] + santa_position[0]
            cl = circle[i][1] + santa_position[1]
            if matrix[rw][cl] == 'V' or matrix[rw][cl] == 'X':
                m -= 1
                if matrix[rw][cl] == 'V':
                    nice_kids += 1
                matrix[rw][cl] = '-'

    matrix[row][col] = '-'  # замествам всички символи по пътя на Santa s '-'
    r, c = santa_position[0], santa_position[1]  # взимам последните координати на Santa

if m == 0 and count_nice_kids - nice_kids > 0:
    print("Santa ran out of presents!")

matrix[r][c] = 'S'  # маркирам с 'S' на последната дестинация на Santa

# разпечатвам матрицата
[print(' '.join(row)) for row in matrix]

if count_nice_kids > nice_kids: # ако останат добри деца без подаръци
    print(f"No presents for {count_nice_kids - nice_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
