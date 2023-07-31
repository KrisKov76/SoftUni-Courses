number_of_pieces = int(input())
dictionary = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split('|')
    dictionary[piece] = [composer, key]

while True:
    command, *params = input().split('|')

    if command == 'Stop':
        break

    elif command == 'Add':
        piece, composer, key = params

        if piece not in dictionary:
            dictionary[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f'{piece} is already in the collection!')

    elif command == 'Remove':
        piece = params[0]

        if piece in dictionary:
            del dictionary[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command.startswith('ChangeKey'):
        piece, new_key = params

        if piece in dictionary:
            dictionary[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key, value in dictionary.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
