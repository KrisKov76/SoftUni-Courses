# for _ in range(3):
#     data = input()
#     my_list.append(data)

# с компрехеншън
my_list = [input() for _ in range(3)]

# swap-ване
my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)




