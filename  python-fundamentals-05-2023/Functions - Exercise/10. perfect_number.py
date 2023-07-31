def is_perfect(number):
    lst = sum([i for i in range(1, number) if number % i == 0])
    if lst == number:
        return "We have a perfect number!"
    return "It's not so perfect."

some_number = int(input())
print(is_perfect(some_number))
