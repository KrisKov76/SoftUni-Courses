def print_row(n, i):
    print(f"{(n - i) * ' '} {i * '* '}")


def triangle(n):
    for i in range(0, n + 1):
        print_row(n, i)


def reverse_triangle(n):
    for i in range(n - 1, 0, -1):
        print_row(n, i)


def rhombus(n):
    triangle(n)
    reverse_triangle(n)


n = int(input())

rhombus(n)