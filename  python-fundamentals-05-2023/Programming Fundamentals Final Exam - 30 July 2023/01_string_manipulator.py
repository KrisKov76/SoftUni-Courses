string = input()

while True:
    command, *params = input().split()

    if command == 'End':
        break

    elif command == 'Translate':
        char, replacement = params
        string = string.replace(char, replacement)
        print(string)

    elif command == 'Includes':
        substring = params[0]
        print('True' if substring in string else 'False')
    elif command == 'Start':
        substring = params[0]
        print('True' if string.startswith(substring) else 'False')
    elif command == 'Lowercase':
        string = string.lower()
        print(string)
    elif command == 'FindIndex':
        char2 = params[0]
        ind = string.rfind(char2)
        print(ind)
    elif command == 'Remove':
        startIndex, count = map(int, params)
        string = string[:startIndex] + string[startIndex + count:]
        print(string)
