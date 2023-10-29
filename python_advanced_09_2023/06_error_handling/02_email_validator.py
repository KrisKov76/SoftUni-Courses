class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ['com', 'org', 'net', 'bg']

while True:
    email = input()

    if email == 'End':
        break

    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    if len(email.split('@')[0]) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    if email.split('.')[-1] not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid" )