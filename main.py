import string
import Exception as ex

def check_input(username, password):
    """
    The function accepts two parameters of type string: username and password. The function prints "OK" to the screen
    if the username and password are correct (that is, meet the conditions presented earlier).
    param: username: A string that the user chooses.
    param: password: A string that the user chooses.
    return: None.
    """
    # Flags
    passSmallLetter = False
    passCapitalLetter = False
    passDigit = False
    passPunc = False
    try:
        if len(username) < 3:
            raise ex.UsernameTooShort(username)
        if len(username) > 16:
            raise ex.UsernameTooLong(username)

        for letter in username:
            if letter not in string.punctuation and not letter.isalpha() and not letter == '_' and not letter.isdigit():
                raise ex.UsernameContainsIllegalCharacter(letter)

        if len(password) < 8:
            raise ex.PasswordTooShort(password)
        if len(password) > 40:
            raise ex.PasswordTooLong(password)

        for letter in password:
            if letter in string.punctuation:
                passPunc = True
            elif letter.islower():
                passSmallLetter = True
            elif letter.isupper():
                passCapitalLetter = True
            elif letter.isdigit():
                passDigit = True

        if not passPunc or not passSmallLetter or not passCapitalLetter or not passDigit:
            raise ex.PasswordMissingCharacter(password)

    except ex.UsernameTooShort as e:
        print("Username longer than 2 characters is required, and instead got %d characters.\n" % len(e.get_arg()))
    except ex.UsernameTooLong as e:
        print("Username shorter than 9 characters is required. The length of the received username is %d.\n"
              % len(e.get_arg()))
    except ex.UsernameContainsIllegalCharacter as e:
        print("Username Must consist one of the following legal characters: English letters, numbers or an "
              "underscore.\n"
              "Instead got the illegal character: %s.\n" % e.get_arg())
    except ex.PasswordTooShort as e:
        print("A password longer than 8 characters is required. The length of the received password is %d.\n"
              % len(e.get_arg()))
    except ex.PasswordTooLong as e:
        print("Password shorter than 41 characters is required, and instead got %s.\n" % len(e.get_arg()))
    except ex.PasswordMissingCharacter as e:
        print("Password must contain at least one of the following mandatory characters: one uppercase English\n "
              "letter, one lowercase English letter, one number and one special character. Instead got the illegal\n "
              "password: %s.\n" % e.get_arg())

    else:
        print("OK")


def main():
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")


if __name__ == "__main__":
    main()

