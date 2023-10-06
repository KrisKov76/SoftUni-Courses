
# def calculate(number_a, number_b, operator):
#     if operator == "multiply":
#         return number_a * number_b
#     elif operator == "divide":
#         return int(number_a / number_b)
#     elif operator == "add":
#         return number_a + number_b
#     elif operator == "subtract":
#         return number_a - number_b

# с използване на речник
def calculate(operator, num1, num2):
    return {
        'multiply': num1 * num2,
        'divide': int(num1/num2),
        'add': num1 + num2,
        'subtract': num1 - num2
    }.get(operator, 'Invalid operator')


operator = input()
num1 = int(input())
num2 = int(input())

print(calculate(operator, num1, num2))