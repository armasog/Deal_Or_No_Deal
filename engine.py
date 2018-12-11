import unittest
import random
import config
import copy

amounts = copy.deepcopy(config.dollar_values)
board_case_numbers = copy.deepcopy(config.case_numbers)
round = 1

def fill_cases():
    cases = {}
    shuffled_amounts = copy.deepcopy(config.dollar_values)
    random.shuffle(shuffled_amounts)
    for i in config.case_numbers:
        cases[i] = shuffled_amounts[i-1]
    return cases


board_cases = fill_cases()  # Fill each case with a dollar value


def print_board():
    print(board_case_numbers)
    print(amounts)

def pick_case():
    global board_case_numbers
    selection = input('Select a case: ')
    try:
        selection = int(selection)
        if selection in board_case_numbers:
            return selection
        else:
            print('Please select a valid case. ')
            return pick_case()
    except ValueError:
        print('Please enter an integer. ')
        return pick_case()

def open_case(case):
    global board_cases, board_case_numbers, amounts
    board_case_numbers[board_case_numbers.index(case)] = 'X'  # Replace opened cases with Xs
    amounts[amounts.index(board_cases[case])] = 'X'  # Replace found amounts with Xs
    return board_cases[case]

def banker_offer():
    global round, amounts
    expected_value = 0
    value_of_all_cases = 0
    cases_outstanding = 0
    sucker_discount = 0.0
    max_value = max([i for i in amounts if isinstance(i, int)])
    for case in board_case_numbers:
        if case != 'X':
            cases_outstanding += 1
    for value in amounts:
        if value != 'X':
            value_of_all_cases += value
    expected_value = value_of_all_cases/cases_outstanding
    #FIXME - Banker formula is all off
    return 12275 + (0.748 * expected_value) + (-0.040 * max_value) + (0.0000006986 * (expected_value*expected_value)) + (32.623 * (cases_outstanding*cases_outstanding))

