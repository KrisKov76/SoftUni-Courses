import math


def closest_point(X1, Y1, X2, Y2):

    dist1 = math.sqrt(X1 ** 2 + Y1 ** 2)
    dist2 = math.sqrt(X2 ** 2 + Y2 ** 2)
    print(dist1, dist2)

    if dist1 <= dist2:
        return f"({math.floor(X1)}, {math.floor(Y1)})"
    else:
        return f"({math.floor(X2)}, {math.floor(Y2)})"

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(closest_point(x1, y1, x2, y2))