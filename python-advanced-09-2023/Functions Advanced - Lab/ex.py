# def multiply(*args):
#     result = 1
#     for num in args:
#         result *= num
#     return result
#
# print(multiply(2, 3, 5))
#
# def greet_me(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}, {value}")
#
# greet_me(Kris="Hello", Georgi="Goodby")

a = {10, -2, 4, 3}
print(a)
print(sorted(a))
print(sorted(a, reverse=True))

my_dict = {'Peter':[20,3], 'Kris': [47,4], 'Deni': [32, 3]}

# for key, value in my_dict.items():
#     print(key, value)

sorted_dict = sorted(my_dict.items(), key=lambda kvp: -kvp[1])

for key, value in sorted_dict:
    print(key, value)