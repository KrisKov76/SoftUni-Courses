entry = input()


def numeric(strings):
    result = [letter for letter in strings if letter.isnumeric()]
    return ''.join(result)


def alpha(strings):
    result = [letter for letter in strings if letter.isalpha()]
    return ''.join(result)


def alnum(strings):
    result = [letter for letter in strings if not letter.isalnum()]
    return ''.join(result)


print(numeric(entry))
print(alpha(entry))
print(alnum(entry))
