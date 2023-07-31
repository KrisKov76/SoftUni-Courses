followers = {}


def new_follower(username):
    followers.setdefault(username, [0, 0])


def likes(username, count):
    followers.setdefault(username, [0, 0])
    followers[username][0] += int(count)


def comments(username):
    followers.setdefault(username, [0, 0])
    followers[username][1] += 1


def blocked(username):
    if username in followers:
        del followers[username]
    else:
        print(f"{username} doesn't exist.")


command, *params = input().split(': ')
while True:

    if command == 'Log out':

        break

    elif command == 'New follower':
        username = params[0]
        new_follower(username)
    elif command == 'Like':
        username, count = params
        likes(username, count)
    elif command == 'Comment':
        username = params[0]
        comments(username)
    elif command == 'Blocked':
        username = params[0]
        blocked(username)

    command, *params = input().split(': ')

print(f'{len(followers)} followers')

for key, value in followers.items():
    print(f'{key}: {sum(value)}')
