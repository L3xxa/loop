


import unittest
from main import multiplication_table
class TestMultiplicationTable(unittest.TestCase):

    # Generates multiplication tables for a valid range of numbers
    def test_valid_range(self):
        with unittest.mock.patch('builtins.input', side_effect=['2', '3']):
            with unittest.mock.patch('builtins.print') as mock_print:
                multiplication_table()
                expected_calls = [
                    unittest.mock.call('2*1=2', end=' '),
                    unittest.mock.call('2*2=4', end=' '),
                    unittest.mock.call('2*3=6', end=' '),
                    unittest.mock.call('2*4=8', end=' '),
                    unittest.mock.call('2*5=10', end=' '),
                    unittest.mock.call('2*6=12', end=' '),
                    unittest.mock.call('2*7=14', end=' '),
                    unittest.mock.call('2*8=16', end=' '),
                    unittest.mock.call('2*9=18', end=' '),
                    unittest.mock.call('2*10=20', end=' '),
                    unittest.mock.call(),
                    unittest.mock.call('3*1=3', end=' '),
                    unittest.mock.call('3*2=6', end=' '),
                    unittest.mock.call('3*3=9', end=' '),
                    unittest.mock.call('3*4=12', end=' '),
                    unittest.mock.call('3*5=15', end=' '),
                    unittest.mock.call('3*6=18', end=' '),
                    unittest.mock.call('3*7=21', end=' '),
                    unittest.mock.call('3*8=24', end=' '),
                    unittest.mock.call('3*9=27', end=' '),
                    unittest.mock.call('3*10=30', end=' '),
                    unittest.mock.call()
                ]
                mock_print.assert_has_calls(expected_calls)

    # Handles negative numbers as input for the range
    def test_negative_numbers(self):
        with unittest.mock.patch('builtins.input', side_effect=['-2', '-1']):
            with unittest.mock.patch('builtins.print') as mock_print:
                multiplication_table()
                expected_calls = [
                    unittest.mock.call('-2*1=-2', end=' '),
                    unittest.mock.call('-2*2=-4', end=' '),
                    unittest.mock.call('-2*3=-6', end=' '),
                    unittest.mock.call('-2*4=-8', end=' '),
                    unittest.mock.call('-2*5=-10', end=' '),
                    unittest.mock.call('-2*6=-12', end=' '),
                    unittest.mock.call('-2*7=-14', end=' '),
                    unittest.mock.call('-2*8=-16', end=' '),
                    unittest.mock.call('-2*9=-18', end=' '),
                    unittest.mock.call('-2*10=-20', end=' '),
                    unittest.mock.call(),
                    unittest.mock.call('-1*1=-1', end=' '),
                    unittest.mock.call('-1*2=-2', end=' '),
                    unittest.mock.call('-1*3=-3', end=' '),
                    unittest.mock.call('-1*4=-4', end=' '),
                    unittest.mock.call('-1*5=-5', end=' '),
                    unittest.mock.call('-1*6=-6', end=' '),
                    unittest.mock.call('-1*7=-7', end=' '),
                    unittest.mock.call('-1*8=-8', end=' '),
                    unittest.mock.call('-1*9=-9', end=' '),
                    unittest.mock.call('-1*10=-10', end=' '),
                    unittest.mock.call()
                ]
                mock_print.assert_has_calls(expected_calls)

    # Manages cases where the start and end numbers are the same
    def test_same_start_end(self):
        with unittest.mock.patch('builtins.input', side_effect=['5', '5']):
            with unittest.mock.patch('builtins.print') as mock_print:
                multiplication_table()
                expected_calls = [
                    unittest.mock.call('5*1=5', end=' '),
                    unittest.mock.call('5*2=10', end=' '),
                    unittest.mock.call('5*3=15', end=' '),
                    unittest.mock.call('5*4=20', end=' '),
                    unittest.mock.call('5*5=25', end=' '),
                    unittest.mock.call('5*6=30', end=' '),
                    unittest.mock.call('5*7=35', end=' '),
                    unittest.mock.call('5*8=40', end=' '),
                    unittest.mock.call('5*9=45', end=' '),
                    unittest.mock.call('5*10=50', end=' '),
                    unittest.mock.call()
                ]
                mock_print.assert_has_calls(expected_calls)