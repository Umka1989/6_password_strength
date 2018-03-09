import getpass
import os.path
import sys


def load_black_list(filepath='black_list.txt'):
    if os.path.exists(filepath):
        with open(filepath) as source_file:
            black_list = source_file.read().upper().split('\n')
    else:
        black_list = []
    return black_list


def is_in_black_list(password, black_list):
    return password.upper() in black_list


def rate_length(password):
    too_small_length = 5
    middle_length = 8
    if len(password) < too_small_length:
        return 0
    elif len(password) < middle_length:
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

    return sum([
        bool(count_of_upper_case_letters),
        bool(count_of_lower_case_letters),
        ])


def rate_for_special_symbols(password):
    multiplier_bonus = 2
    count_of_special_symbols = sum(
        1 for symbol in password if symbol.isalnum())
    return bool(count_of_special_symbols) * multiplier_bonus


def count_result(password, black_list):
    bonus_for_all_passed = 1
    score = 1
    if is_in_black_list(password, black_list) == 1:
        return 0
    else:
        score += sum([
            rate_length(password),
            is_all_digits(password),
            is_all_letters(password),
            rate_for_camel_case(password),
            rate_for_special_symbols(password),
        ])
    score = (score if score < 9 else score + bonus_for_all_passed)
    return score


def print_result(score):
    print('On scale of 1 to 10 your password got {}'.format(score))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        black_list = load_black_list(sys.argv[1])
    else:
        black_list = load_black_list()

    password = getpass.getpass('Please enter your password')
    score = count_result(password, black_list)
    print_result(score)
