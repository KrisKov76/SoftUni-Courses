def move(message, number_of_letters):
    moved_part = message[:number_of_letters]
    moved_text = message[number_of_letters:] + moved_part
    return moved_text


def insert(message, index, value):
    sliced_text = message[:index] + value + message[index:]
    return sliced_text


def change_all(message, substring, replacement):
    message = message.replace(substring, replacement)
    return message


encrypted_message = input()
message = encrypted_message

while True:
    command, *params = input().split('|')

    if command == 'Decode':
        print(f"The decrypted message is: {message}")
        break

    elif command == 'Move':
        number_of_letters = params[0]
        message = move(message, int(number_of_letters))
        pass

    elif command == 'Insert':
        index, value = params
        message = insert(message, int(index), value)

    elif command == 'ChangeAll':
        substring, replacement = params
        message = change_all(message, substring, replacement)
