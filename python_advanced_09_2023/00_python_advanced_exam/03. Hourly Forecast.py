def forecast(*args):
    order = {"Sunny": 0, "Cloudy": 1, "Rainy": 2}

    collection = {}

    for arg in args:
        # town = arg[0]
        # weather = arg[1]
        town, weather = arg

        if weather not in collection:
            collection[weather] = []
        collection[weather].append(town)

    result = ''

    for key in sorted(collection.keys(), key=lambda k: order[k]):
        sorted_value = sorted(collection[key])
        for town in sorted_value:
            result += f"{town} - {key}\n"

    return result
