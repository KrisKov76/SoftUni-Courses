registered_numbers = {}

count = int(input())

for i in range(count):
    entry = input().split()

    if entry[0] == 'register':
        command, username, plate_number = entry[0], entry[1], entry[2]

        if username not in registered_numbers:
            registered_numbers[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")

    elif entry[0] == 'unregister':
        command, username = entry[0], entry[1]
        if username in registered_numbers:
            poped_name = registered_numbers.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for key, value in registered_numbers.items():
    print(f'{key} => {value}')
