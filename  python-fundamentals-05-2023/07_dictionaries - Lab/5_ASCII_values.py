lst = input().split(', ')

my_dict = {x: ord(x) for x in lst}
print(my_dict)