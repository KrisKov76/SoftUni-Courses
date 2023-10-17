def words_sorting(*args):
    dict_ = {}
    total_sum = 0

    for arg in args:
        if arg not in dict_:
            dict_[arg] = 0
        ord_arg = sum([ord(x) for x in arg])
        dict_[arg] += ord_arg
        total_sum += ord_arg

    result = ''

    if total_sum % 2 == 0:
        for key, value in sorted(dict_.items(), key=lambda a: a[0]):
            result += f"{key} - {value}\n"
    else:
        for key, value in sorted(dict_.items(), key=lambda a: -a[1]):
            result += f"{key} - {value}\n"

    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
