def start_spring(**kwargs):
    collection = {}

    for key, value in kwargs.items():
        if value not in collection:
            collection[value] = []
        collection[value].append(key)

    sorted_dict = dict(sorted(collection.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    result = []

    for key, value in sorted_dict.items():
        sorted_values = sorted(value) # допълнително сортиране на стойностите по азбучен ред
        new_value = '\n'.join([f'-{item}' for item in sorted_values]) # итериране на стойностите на нов ред с тире отпред
        result.append(f'{key}:')
        result.append(f'{new_value}')

    return '\n'.join(result)


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))



