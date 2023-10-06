def take_odd(my_string):
    lst = [x for x in my_string]
    odd_ind = [v for i, v in enumerate(lst) if i % 2 != 0]
    return ''.join(odd_ind)


def cut_string(password, my_index, my_length):
    sliced_part = password[my_index: my_index + my_length]
    sliced_string = password.replace(sliced_part, '', 1)
    return sliced_string


def substitute_string(password, substring, substitute):
    replaced_string = password.replace(substring, substitute)
    return replaced_string


string = input()
password = string

while True:
    command, *params = input().split()

    if command == 'Done':
        print(f"Your password is: {password}")
        break

    elif command == 'TakeOdd':
        password = take_odd(password)
        print(password)

    elif command == 'Cut':
        index, length = params
        password = cut_string(password, int(index), int(length))
        print(password)

    elif command == 'Substitute':
        substring, substitute = params
        if substring in password:
            password = substitute_string(password, substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
