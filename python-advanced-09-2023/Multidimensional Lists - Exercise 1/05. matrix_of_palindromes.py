# и това e толкова, матрица, колкото аз съм лисица

rows, cols = [int(x) for x in input().split()]

lst = []

for i in range(rows):
    for i2 in range(cols):
        print(f"{chr(97 + i)}{chr(97 + i + i2)}{chr(97 + i)}", end=' ')
    print()
