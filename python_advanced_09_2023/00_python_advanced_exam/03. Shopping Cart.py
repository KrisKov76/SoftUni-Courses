def shopping_cart(*args):
    collection = {'Pizza': [], 'Soup': [], 'Dessert': []}

    for arg in args:
        if arg == 'Stop':
            break
        elif arg[0] == 'Pizza' and len(collection['Pizza']) < 4 and arg[1] not in collection['Pizza']:
            collection['Pizza'].append(arg[1])
        elif arg[0] == 'Soup' and len(collection['Soup']) < 3 and arg[1] not in collection['Soup']:
            collection['Soup'].append(arg[1])
        elif arg[0] == 'Dessert' and len(collection['Dessert']) < 2 and arg[1] not in collection['Dessert']:
            collection['Dessert'].append(arg[1])
        else:
            continue

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