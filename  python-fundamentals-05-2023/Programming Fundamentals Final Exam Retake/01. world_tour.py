def add_stop(result, index, string):
    sliced_string = result[:index] + string + result[index:]
    return sliced_string


def remove_stop(result, start_index, end_index):
    changed_string = result[:start_index] + result[end_index + 1:]
    return changed_string


def switch(result, old_string, new_string):
    switched_string = result.replace(old_string, new_string)
    return switched_string


text = input()
result = text

while True:
    command, *params = input().split(':')

    if command == 'Travel':
        print(f'Ready for world tour! Planned stops: {result}')
        break

    elif command == 'Add Stop':
        index, string = params
        if 0 <= int(index) <= len(text):
            result = add_stop(result, int(index), string)
        print(result)

    elif command == 'Remove Stop':
        start_index, end_index = params
        if 0 <= int(start_index) <= len(text) and 0 <= int(end_index) <= len(text):
            result = remove_stop(result, int(start_index), int(end_index))
        print(result)

    elif command == 'Switch':
        old_string, new_string = params
        if old_string in result:
            result = switch(result, old_string, new_string)
        print(result)

