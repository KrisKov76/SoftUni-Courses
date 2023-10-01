# a = [int(el) for el in input().split(", ")]
#
# index = int(input())
#
# try:
#     print(a[index])
# except IndexError:
#     print('Invalid index, try again!')


class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    number = float(input())
    if number < 0:
        raise ValueCannotBeNegative
