# def loading_bar(percent):
#     start_index = percent // 10
#     for i in range(11):
#         increasing_percentage = start_index * "%" + (10 - start_index) * "."
#
#     if percent < 100:
#         return f'{percent}% [{increasing_percentage}]\nStill loading...'
#     return '100% Complete!\n[%%%%%%%%%%]'
#
#
# percent_choise = int(input())
# print(loading_bar(percent_choise))

def loading_bar(percent):
    bars = ["%" if i < percent // 10 else "." for i in range(10)]
    bar_string = "".join(bars)

    if percent < 100:
        return f"{percent}% [{bar_string}]\nStill loading..."
    return "100% Complete!\n[%%%%%%%%%%]"


percent_choice = int(input())
print(loading_bar(percent_choice))

# Изводи:
#1. Целочислено деление //. Не съм съобразил, че с две черти може да делим целочислено, без да се налага да слагаме int

# a = int(60 /  10)
# print(a)
#
# a = 60 // 10
# print(a)

#2. Не е нужно да използвам средни скоби () след return. Не е нужно също да използвам f, когато нямам {} къдрави скоби

#3.

# bars = ["%" if i <= percent // 10 else "." for i in range(11)]
# bar_string = "".join(bars)
# print(bars)
# print(bar_string)

# percent = 100
# for i in range(11):
#     if i < 1:
#         print('%', end='')
#     else:
#         print('.', end='')