def even_numbers(n): # името на функцията на декоратора седи най-отгоре
    def decorator(function): # имаме def decorator, защото е троен
        def wrapper(*args, **kwargs): # задължително wrapper-ът, който репрезентира функцията да е с *args, **kwargs!!!
            result = function(*args, **kwargs)
            return [num for num in result if num % 2 == 0] * n
        return wrapper # върни ми референция към wrapper
    return decorator # върни ми референция към самия декоратор


@even_numbers(1) # аргумент в декоратора - три функции (троен декоратор)
def get_numbers(numbers):
    return numbers