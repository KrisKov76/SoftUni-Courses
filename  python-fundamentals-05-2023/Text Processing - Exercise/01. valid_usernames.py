entry = input().split(', ')


def valid_length(username):
    if 3 <= len(username) <= 16:
        return True

def valid_char(username):
    if username.isalnum() or '-' in username or '_' in username:
        return True

def not_space(username):
    if ' ' in username:
        return False
    return True

result = [word for word in entry if valid_length(word) and valid_char(word) and not_space(word)]
print('\n'.join(result))
