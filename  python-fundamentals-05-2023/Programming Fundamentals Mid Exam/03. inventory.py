# 100.0

lst = input().split(', ')

while True:
    command = input()

    if command == 'Craft!':
        break

    command = command.split(' - ')

    command_todo, item = command[0], command[1]

    if command_todo == 'Collect':
        if item not in lst:
            lst.append(item)
    elif command_todo == 'Drop':
        if item in lst:
            lst.remove(item)
    elif command_todo == 'Combine Items':
        old_new = item.split(':')
        old, new = old_new[0], old_new[1]
        if old in lst:
            new_index = lst.index(old)
            lst.insert(new_index + 1, new)
    elif command_todo == 'Renew':
        if item in lst:
            lst.remove(item)
            lst.append(item)

print(*lst, sep=', ')
