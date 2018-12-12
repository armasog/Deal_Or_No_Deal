import mock
import unittest
import game_engine as ge


class TestSuite(unittest.TestCase):
    def test_pick_case_valid_number(self):
        with mock.patch('builtins.input', return_value=2):
            assert ge.pick_case() == 2
            ge.board_case_numbers[1] = 2  # Reset the application after test is complete

    def test_x_out_opened_case(self):
        with mock.patch('builtins.input', return_value=2):
            picked_case = ge.pick_case()
            amounts_index = ge.amounts.index(ge.board_cases[picked_case])
            original_amount = ge.amounts[amounts_index]
            ge.open_case(picked_case)
            assert ge.board_case_numbers[1] == 'X'
        ge.amounts[amounts_index] = original_amount  # Reset the application after test is complete

    def test_deal_or_no_deal_bool(self):
        with mock.patch('builtins.input', return_value='D'):
            assert ge.deal_or_no_deal() == True
