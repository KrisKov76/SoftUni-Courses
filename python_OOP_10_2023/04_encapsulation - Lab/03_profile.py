class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) >= 5 and len(value) <= 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_valid_name = len(value) >= 8
        is_upper = any([char for char in value if char.isupper()])
        is_digit = any([char for char in value if char.isdigit()])

        if is_valid_name and is_upper and is_digit:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more "
                             "characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return (f'You have a profile with username: "{self.username}"'
                f' and password: {"*" * len(self.password)}')

profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)
