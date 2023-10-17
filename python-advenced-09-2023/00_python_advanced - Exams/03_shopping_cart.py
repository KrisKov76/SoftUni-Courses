def shopping_cart(*args):
    collection = {'Pizza': [], 'Soup': [], 'Dessert': []}

    for arg in args:
        if arg == 'Stop':
            break
        elif arg[0] == 'Pizza' and len(collection['Pizza']) == 4:
            continue
        elif arg[0] == 'Soup' and len(collection['Soup']) == 3:
            continue
        elif arg[0] == 'Dessert' and len(collection['Dessert']) == 2:
            continue
        if arg[1] not in collection[arg[0]]: 
            collection[arg[0]].append(arg[1])

    sorted_list = sorted(collection.items(), key=lambda a: (-len(a[1]), a[0]))

    result = ''
    for k, v in sorted_list:
        result += f"{k}:\n"
        sorted_product = sorted(v)
        for item in sorted_product:
            result += f" - {item}\n"

    for value in collection.values():
        if len(value) > 0:
            return result
    else:
        return "No products in the cart!"

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
