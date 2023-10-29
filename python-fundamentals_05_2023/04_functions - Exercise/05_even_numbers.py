def even_numbers(num):
    numbers = list(map(int, num.split()))
    even_num = [n for n in numbers if n % 2 == 0]
    return even_num


number_two = input()
print(even_numbers(number_two))
