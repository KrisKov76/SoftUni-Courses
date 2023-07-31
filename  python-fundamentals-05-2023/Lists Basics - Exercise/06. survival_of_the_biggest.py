
lst = input().split()
lst_digit = []
number = int(input())

# превръщане на елементите от string в integer
for element in lst:
    lst_digit.append(int(element))

# премахване на най-малките числа - number на брой
for _ in range(number):
    min_num = 1000
    for i in range(len(lst_digit)):
        if lst_digit[i] < min_num:
            min_num = lst_digit[i]
    lst_digit.remove(min_num)

print(*lst_digit, sep=", ")
