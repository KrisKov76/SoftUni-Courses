def contains_function(substring, raw):
    if substring in raw:
        return f'{raw} contains {substring}'
    return (f'Substring not found!')


def slice_function(raw, startIndex, endIndex):
    new_raw = raw[:int(startIndex)] + raw[int(endIndex):]
    return new_raw


def flip_function(raw, upperlower, index_one, index_two):
    if upperlower == 'Upper':
        sliced_raw = raw[int(index_one):int(index_two)]
        uppered_sliced_raw = sliced_raw.upper()
        new_raw = raw[:int(index_one)] + uppered_sliced_raw + raw[int(index_two):]
        return new_raw

    elif upperlower == 'Lower':
        sliced_raw = raw[int(index_one):int(index_two)]
        lower_sliced_raw = sliced_raw.lower()
        new_raw = raw[:int(index_one)] + lower_sliced_raw + raw[int(index_two):]
        return new_raw


activation_key = input()

while True:
    command, *params = input().split('>>>')

    if command == 'Generate':
        print(f'Your activation key is: {activation_key}')
        break

    elif command == 'Contains':
        substring = params[0]
        message = contains_function(substring, activation_key)
        print(message)

    elif command == 'Slice':
        startIndex, endIndex = params
        activation_key = slice_function(activation_key, startIndex, endIndex)
        print(activation_key)

    elif command == 'Flip':
        upperlower, index_one, index_two = params
        activation_key = flip_function(activation_key, upperlower, index_one, index_two)
        print(activation_key)
