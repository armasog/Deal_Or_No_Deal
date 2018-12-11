import mock
import unittest
import game_engine as ge


class TestSuite(unittest.TestCase):
    def test_pick_case_valid_number(self):
        with mock.patch('builtins.input', return_value=2):
            assert ge.pick_case() == 2

    def test_x_out_opened_case(self):
        with mock.patch('builtins.input', return_value=1):
            ge.open_case(ge.pick_case())
        assert ge.board_case_numbers[0] == 'X'

    def test_deal_or_no_deal_bool(self):
        with mock.patch('builtins.input', return_value='D'):
            assert ge.deal_or_no_deal() == True
