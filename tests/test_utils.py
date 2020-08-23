import unittest

import dazspark.utils as u


class TestUtilsColumnNameCleaning(unittest.TestCase):
    def test_removal_of_spaces(self):
        input: str = "Example Column Name"
        expected: str = "Example_Column_Name"
        self.assertEqual(expected, u.replace_invalid_chars(input))
