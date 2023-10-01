def age_assignment(*args, **kwargs):
    persons = {}
    for name in args:
        persons[name] = kwargs[name[0]]
    result = sorted(persons.items(),key=lambda kvp:kvp[0])
    final_result = []

    for key, value in result:
        final_result.append(f'{key} is {value} years old.')
    return '\n'.join(final_result)



print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))