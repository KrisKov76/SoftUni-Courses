def accommodate_new_pets(*args):
    capacity = int(args[0])
    max_weight = float(args[1])
    collection = {}
    result = []

    for pet_type, pet_weight in args[2:]:
        if capacity <= 0:
            result.append('You did not manage to accommodate all pets!')
            break
        if pet_weight > max_weight:
            continue
        if pet_type not in collection:
            collection[pet_type] = 0
        collection[pet_type] += 1
        capacity -= 1
    else:
        result.append(f'All pets are accommodated! Available capacity: {capacity}.')

    result.append('Accommodated pets:')
    [result.append(f'{pet_type}: {pet_number}') for pet_type, pet_number in sorted(collection.items())]
    return '\n'.join(result)


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
