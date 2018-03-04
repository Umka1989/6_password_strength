import sys


black_list = [
    '123456789',
    'admin',
    'qwerty',
    'password',
    'qweasd',
]


def is_in_black_list(password):
    if password in black_list:
        return 0
    else:
        return 1


def length_checker(password):
    if len(password) < 5:
        return 0
    elif len(password) < 8:
        return 1
    else:
        return 2


def is_all_digits(password):
    if len(password) == sum(1 for symbol in password if symbol.isdigit()):
        return 0
    else:
        return 1


def is_all_letters(password):
    if len(password) == sum(1 for symbol in password if symbol.isalpha()):
        return 0
    else:
        return 1


def is_camel_case(password):
    count_of_upper_case_letters = sum(
        1 for symbol in password if symbol.isupper())
    count_of_lower_case_letters = sum(
        1 for symbol in password if symbol.lower())

    if count_of_upper_case_letters > 0 and count_of_lower_case_letters > 0:
        return 2
    elif count_of_upper_case_letters > 0 or count_of_lower_case_letters > 0:
        return 1
    else:
        return 0


def has_special_symbols(password):
    count_of_special_symbols = sum(
        1 for symbol in password if symbol.isalnum())
    if count_of_special_symbols in range(len(password)):
        return 2
    elif count_of_special_symbols > 0:
        return 1
    else:
        return 0


def get_password_strength(password):
    score = 1
    if is_in_black_list(password) == 0:
        return 0
    else:
        score += length_checker(password)
        score += is_all_digits(password)
        score += is_all_letters(password)
        score += is_camel_case(password)
        score += has_special_symbols(password)
    # if all tests are passed we add 1 bonus point to final score
    score = (score if score < 9 else 10)
    print('On scale of 1 to 10 your password got {}'.format(score))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("program need one argument - password")
    else:
        get_password_strength(sys.argv[1])
