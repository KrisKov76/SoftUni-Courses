# def check_password(password):
#     # с използване на булева променлива
#     pass_valid = True
#
#     # if len(password) < 6 or len(password) > 10:
#     if len(password) not in range(6, 11): # това е много по-тарикатско!
#         pass_valid = False
#         print("Password must be between 6 and 10 characters")
#     if not password.isalnum():
#         pass_valid = False
#         print("Password must consist only of letters and digits")
#     # if sum(c.isdigit() for c in password) < 2:
#     if sum(1 for c in password if c.isdigit()) < 2: # и това е тарикатско!
#         pass_valid = False
#         print("Password must have at least 2 digits")
#     return pass_valid
#
# password = input()
# pass_valid = check_password((password))
# if pass_valid == True:
#     print("Password is valid")


# Нека разбием тази функция на няколко по-малки, за да е по-четимо

def lenth_validation(password):
    if len(password) not in range(6, 11):  # това е много по-тарикатско!
        print("Password must be between 6 and 10 characters")
        return False
    return True

def symbol_validation(password):
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        return False
    return True

def digits_validation(password):
    if sum(1 for c in password if c.isdigit()) < 2: # и това е тарикатско!
        print("Password must have at least 2 digits")
        return False
    return True

some_password = input()
is_valid = [lenth_validation(some_password), symbol_validation(some_password), digits_validation(some_password) ]

# if not False in is_valid:
#     print("Password is valid")

if all(is_valid): # супер тарикатско - ползваш един лист, в който поставяш всички функции, ползваш all, което дава True,
    # само ако всички функции вътре връщат True
    print("Password is valid")