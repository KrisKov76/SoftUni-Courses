# numbers = input().split(', ')
#
# positive_nums = [num for num in numbers if int(num) >= 0]
# negative_nums = [num for num in numbers if int(num) < 0]
# even_nums = [num for num in numbers if int(num) % 2 == 0]
# odd_nums = [num for num in numbers if int(num) % 2 != 0]
#
# print(f"Positive: {', '.join(positive_nums)}")
# print(f"Negative: {', '.join(negative_nums)}")
# print(f"Even: {', '.join(even_nums)}")
# print(f"Odd: {', '.join(odd_nums)}")

#2 вариант - с използване на функции

def positive_numbers(some_numbers):
    return [num for num in some_numbers if int(num) >= 0]

def negative_numbers(some_numbers):
    return [num for num in some_numbers if int(num) < 0]

def even_numbers(some_numbers):
    return [num for num in some_numbers if int(num) % 2 == 0]

def odd_numbers(some_numbers):
    return [num for num in some_numbers if int(num) % 2 != 0]

numbers = input().split(', ')

print(f"Positive: {', '.join(positive_numbers(numbers))}")
print(f"Negative: {', '.join(negative_numbers(numbers))}")
print(f"Even: {', '.join(even_numbers(numbers))}")
print(f"Odd: {', '.join(odd_numbers(numbers))}")