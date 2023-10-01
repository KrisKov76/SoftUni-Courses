def operate(sign, *args):
    def add():
        return sum(args)

    def subtract():
        result = 0
        for el in args:
            result -= el
        return result

    def multiply():
        result = 1
        for el in args:
            result *= el
        return result

    def devide():
        result = 1
        for el in args:
            result /= el
        return result

    if sign == "+":
        return add()
    elif sign == '-':
        return subtract()
    elif sign == '*':
        return multiply()
    elif sign == '/':
        return devide()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
