def sorted_numbers(num):
    numbers = list(map(int, num.split()))
    sorted_num = sorted(numbers)
    return sorted_num

numbers = input()
print(sorted_numbers(numbers))