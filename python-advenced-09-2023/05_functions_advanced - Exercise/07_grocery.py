def grocery_store(**kwargs):
    sorted_dict = dict(sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0])))
    result = []
    for key, value in sorted_dict.items():
        result.append(f'{key}: {value}')
    return '\n'.join(result)
