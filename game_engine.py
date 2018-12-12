import random
import config
import copy
import time

amounts = copy.deepcopy(config.dollar_values)
board_case_numbers = copy.deepcopy(config.case_numbers)
game_round = 1
past_offers = []
game_over = False


def fill_cases():
    cases = {}
    shuffled_amounts = copy.deepcopy(config.dollar_values)
    random.shuffle(shuffled_amounts)
    for i in config.case_numbers:
        cases[i] = shuffled_amounts[i - 1]
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
            board_case_numbers[board_case_numbers.index(selection)] = 'X'  # Replace opened cases with Xs
            return selection
        else:
            print('Please select a valid case. ')
            return pick_case()
    except ValueError:
        print('Please enter an integer. ')
        return pick_case()


def open_case(case):
    global board_cases, board_case_numbers, amounts
    amounts[amounts.index(board_cases[case])] = 'X'  # Replace found amounts with Xs
    return board_cases[case]


def banker_offer():
    global amounts, round
    value_of_all_cases = 0
    cases_outstanding = 1  # Starts at one to account for the player's selected case
    for case in board_case_numbers:
        if case != 'X':
            cases_outstanding += 1
    for value in amounts:
        if value != 'X':
            value_of_all_cases += value
    expected_value = value_of_all_cases / cases_outstanding
    # Sucker discount exists so that offers start well below the EV and approach it as the game goes on
    # There is an element of randomness so that offers are not predictable and are more similar to the show
    sucker_discount = (0.73 / (float(game_round) + (random.uniform(-0.15, 0.15))))
    final_offer = expected_value * (1 - sucker_discount)
    return final_offer


def deal_or_no_deal():
    decision = input('Deal (D)... or No Deal(any key)?')
    decision = decision.upper()
    return decision == 'D'


def exit_game(winnings):
    global game_over
    print('Congratulations! You have finished the game with {}'.format(winnings))
    game_over = True


def play_round(number_to_open):
    global past_offers, game_over, game_round
    if not game_over:
        i = 1
        print('Please select {} cases!'.format(number_to_open))
        while i <= number_to_open:
            print(open_case(pick_case()))
            print_board()
            i += 1
        print('What a round! Time to hear the banker\'s offer..')
        time.sleep(5)
        offer = round(banker_offer())
        print('Past offers: ')
        print(past_offers)
        print('The banker offers: {}'.format(offer))
        if deal_or_no_deal():
            exit_game(offer)
        else:
            past_offers.append(offer)
            game_round += 1
