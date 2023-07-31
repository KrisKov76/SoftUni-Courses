def factorial_division(number):
    for i in range(1, number):
        number *= i
    return number


first = int(input())
second = int(input())

first_number = factorial_division((first))
second_number = factorial_division((second))

result = (f'{(first_number / second_number):.2f}')
print(result)
