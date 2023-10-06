
command = input()

while True:

    if command == "End":
        break

    if command != "SoftUni":
        x = [x * 2 for x in command]
        print(''.join(x))

    command = input()