import unittest
from my_numbers import add


class TestMyNumbers(unittest.TestCase):

    def test_int_add(self):
        self.assertEqual(add(1, 1), 2)
