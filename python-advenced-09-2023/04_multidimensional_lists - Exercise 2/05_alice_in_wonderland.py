n = int(input())

matrix = []
alice = []

for row in range(n):
    matrix.append(input().split())
        # къде е Алис?
    for col in range(n):
        if matrix[row][col] == 'A':
            matrix[row][col] = '*'
            alice = [row, col]

# възможни ходове - нагоре, надолу, наляво, надясно, пазени в един речник
possible_moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

# трупаме чайчетата, събрани от Алис
tea_bags = 0

while tea_bags < 10:  # условие за прекратяване на цикъла - събрани 10 чайчета
    command = input()  # четем командите
    move = possible_moves[command]  # движение накъде
    row = alice[0] + move[0]
    col = alice[1] + move[1]

    # кога прекъсваме цикъка - когато излезем извън матрицата или ако попаднем на 'R' - заешката дупка
    if row < 0 or row >= n or col < 0 or col >= n:
        break
    if matrix[row][col] == 'R':
        matrix[row][col] = '*'
        break

    if matrix[row][col] not in '*.':  # ако не е звездичка/точка, значи е число(чай), събираме чай и заместваме със *
        tea_bags += int(matrix[row][col])
    matrix[row][col] = '*'
    alice = [row, col]

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print('Alice didn\'t make it to the tea party.')

# разпечатване на матрицата
[print(' '.join(row)) for row in matrix]
