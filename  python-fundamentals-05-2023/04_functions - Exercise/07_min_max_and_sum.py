def min_max_sum(num):
    numbers = list(map(int, num.split()))
    return min(numbers), max(numbers), sum(numbers)


string_numbers = input()
min_num, max_num, sum_num = min_max_sum(string_numbers) # взимам си ги поотделно

print(f'The minimum number is {min_num}')
print(f'The maximum number is {max_num}')
print(f'The sum number is: {sum_num}')
