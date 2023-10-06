# string = [x for x in input().strip()]
string = tuple(input()) # ако го направя на tuple също ще го разбие на символи
my_dict = {}

for char in string:
    a = string.count(char)
    my_dict[char] = a

sorted_string = sorted(my_dict.items(), key=lambda x: x[0])

for key, value in sorted_string:
    print(f'{key}: {value} time/s')