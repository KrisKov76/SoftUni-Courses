def even_parameters(function):
    def wrapper(*args, **kwargs):
        if any(not isinstance(arg, int) or arg % 2 != 0 for arg in args):
            return 'Please use only even numbers!'
        else:
            result = function(*args, **kwargs)
            return result
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

#
print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
