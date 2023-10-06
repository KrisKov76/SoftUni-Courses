def insert_space_at_index(word, index):
    return word[:index] + ' ' + word[index:]


def change_all(message, substring, replacement):
    modified_word = message.replace(substring, replacement)
    return modified_word


def reverse(string):
    return string[::-1]


concealed_message = input()
message = concealed_message

while True:
    command = input().split(':|:')

    if command[0] == 'Reveal':
        break

    elif command[0] == 'Reverse':
        substring = command[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            message += reverse(substring)
            print(message)
        else:
            print('error')

    elif command[0] == 'InsertSpace':
        index = int(command[1])
        message = insert_space_at_index(message, index)
        print(message)

    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        message = change_all(message, substring, replacement)  # Приложи ChangeAll към текущия message
        print(message)

print(f'You have a new text message: {message}')
