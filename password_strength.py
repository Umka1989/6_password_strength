import getpass
import os.path
import sys


def load_black_list(filepath='black_list.txt'):
    if os.path.exists(filepath):
        with open(filepath) as source_file:
            black_list = source_file.read().upper().split()
    else:
        black_list = []
    return black_list


def is_in_black_list(password):
    return password.upper() in black_list


def rate_length(password):
    if len(password) < 5:
        return 0
    elif len(password) < 8:
        return 1
    else:
        return 2


def is_all_digits(password):
    return password.isdigit()


def is_all_letters(password):
    return password.isalpha()


def rate_for_camel_case(password):
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


def rate_for_special_symbols(password):
    count_of_special_symbols = sum(
        1 for symbol in password if symbol.isalnum())
    if count_of_special_symbols in range(len(password)):
        return 2
    elif count_of_special_symbols > 0:
        return 1
    else:
        return 0


def result_counter(password):
    bonus_for_all_passed = 1
    score = 1
    if is_in_black_list(password) == 1:
        return 0
    else:
        score += sum([length_checker(password),
                     is_all_digits(password),
                     is_all_letters(password),
                     is_camel_case(password),
                     has_special_symbols(password)])
    score = (score if score < 9 else score + bonus_for_all_passed)
    return score


def get_password_strength(score):
    print('On scale of 1 to 10 your password got {}'.format(score))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        black_list = load_black_list(sys.argv[1])
    else:
        black_list = load_black_list()

    password = getpass.getpass('Please enter your password')
    score = result_counter(password)
    get_password_strength(score)
