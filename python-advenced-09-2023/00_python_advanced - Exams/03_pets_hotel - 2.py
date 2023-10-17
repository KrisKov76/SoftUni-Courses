def accommodate_new_pets(*args):
    capacity = int(args[0])
    max_weight = float(args[1])
    collection = {}

    result = ''

    for pet_type, pet_weight in args[2:]:
        if capacity <= 0:
            result += 'You did not manage to accommodate all pets!\n'
            break
        if pet_weight > max_weight:
            continue
        if pet_type not in collection:
            collection[pet_type] = []
        collection[pet_type].append(pet_weight)
        capacity -= 1
    else:
        result += f'All pets are accommodated! Available capacity: {capacity}.\n'

    result += 'Accommodated pets:\n'

    for pet_type, pet_number in sorted(collection.items()):
        result += f"{pet_type}: {len(pet_number)}\n"

    return result


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
