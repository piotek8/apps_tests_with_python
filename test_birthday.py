import unittest
import datetime
from unittest.mock import patch

from main_birthday import compute_days_between_dates, get_user_input, check_is_in_range


class BirthdayAppTestCase(unittest.TestCase):
    def test_compute_days_between_dates(self):
        date1 = datetime.date(2023, 6, 1)
        date2 = datetime.date(2023, 6, 15)
        expected_result = 14
        self.assertEqual(compute_days_between_dates(date1, date2), expected_result)

        date3 = datetime.date(2023, 6, 15)
        date4 = datetime.date(2023, 6, 1)
        expected_result = -14
        self.assertEqual(compute_days_between_dates(date3, date4), expected_result)

    def test_invalid_elements_in_date(self):
        invalid_inputs = ('2023', '6', '31')

        with patch('builtins.input', side_effect=invalid_inputs):
            with self.assertRaises(ValueError):
                get_user_input()

    def test_check_is_in_range(self):
        with self.assertRaises(ValueError):
            check_is_in_range(150, 1000, 2000)

#testy na check month,day,year

if __name__ == '__main__':
    unittest.main()
