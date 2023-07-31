#
# def repeat_string(current_string, number_of_repeating):
#     return current_string * number_of_repeating
#
# string = input()
# number = int(input())
# print(repeat_string(string, number))

string = input()
number = int(input())
result = lambda string, num: string * num
print(result(string, number))