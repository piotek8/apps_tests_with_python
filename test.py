"""
from main import guess_number
import unittest

class TestGuessNumber(unittest.TestCase):

    def too_low(self):
        the_number = random.randint(0, 100)
        result = guess_number(the_number - 1, the_number)
        self.assertEqual(result, 'Too low')

    def too_high(self):
        the_number = random.randint(0, 100)
        result = guess_number(the_number + 1, the_number)
        self.assertEqual(result, 'Too high')

    def win_game(self):
        the_number = random.randint(0, 100)
        result = guess_number(the_number, the_number)
        self.assertEqual(result, 'You win this game')
"""

import unittest
import random
from main import guess_number


class GuessNumberTestCase(unittest.TestCase):
    def setUp(self):
        self.the_number = 50

    def test_guess_number_lower(self):
        result = guess_number(49, self.the_number)
        self.assertEqual(result, 'Too low')

    # 80 jesli jest rozne od self.the_number i liczba znajduje sie powyzej
    def test_guess_number_higher(self):
        result = guess_number(80, self.the_number)
        self.assertEqual(result, 'Too high')

    # 80 jesli jest rozne od self.the_number i liczba znajduje sie powyzej
    def test_guess_number_correct(self):
        result = guess_number(self.the_number, self.the_number)
        self.assertEqual(result, 'You win this game')

    def test_guess_number_invalid_format(self):
        with self.assertRaises(ValueError):
            guess_number('', self.the_number)

    def test_guess_number_invalid_guess(self):
        with self.assertRaises(ValueError):
            guess_number(-1, self.the_number)

        with self.assertRaises(ValueError):
            guess_number(101, self.the_number)

'''
ATTEMPT IN JAVA
    @ParameterizedTest
    @TestSurce(ints = {-1, 101, 103, -5})
    void testcos(int zgaduj) {
        assertExceptionOfType(ValueError.class).isThrown(() -> (guess_number(zgaduj)).withMessage("Invalid value out of range"))
    }
'''

# jesli jest rozne od self.the_number


if __name__ == '__main__':
    unittest.main()
