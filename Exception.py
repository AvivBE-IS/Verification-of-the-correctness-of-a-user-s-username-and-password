class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Username" + str(self.get_arg(self)) + "contains invalid characters."

    def get_arg(self):
        return self._arg


class UsernameTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Provided username %s is shorter than 3 characters." % self._arg

    def get_arg(self):
        return self._arg


class UsernameTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Username" + str(self.get_arg(self)) + "too long."

    def get_arg(self):
        return self._arg


class PasswordMissingCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "The password" + str(self.get_arg(self)) + "does not contain at least one of the required characters."

    def get_arg(self):
        return self._arg


class PasswordTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Password" + str(self.get_arg(self)) + "too short."

    def get_arg(self):
        return self._arg


class PasswordTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Password" + str(self.get_arg(self)) + "too long."

    def get_arg(self):
        return self._arg

