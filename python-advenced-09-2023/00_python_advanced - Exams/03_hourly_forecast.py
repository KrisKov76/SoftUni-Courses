def forecast(*args):
    order = {"Sunny": 0, "Cloudy": 1, "Rainy": 2} # създаваме конкретен ордер

    collection = {}

    for arg in args:
        town, weather = arg

        if weather not in collection:
            collection[weather] = []
        collection[weather].append(town)

    result = ''

    # с помощ от chat.gpt
    for key in sorted(collection.keys(), key=lambda k: order[k]): # сортираме ключовете с итерация през ордера
        sorted_value = sorted(collection[key]) # сортираме values алфабетикал
        for town in sorted_value:
            result += f"{town} - {key}\n" # принтираме

    return result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
