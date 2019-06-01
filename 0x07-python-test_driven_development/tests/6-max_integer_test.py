#!/usr/bin/python3

"""
Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_one_num(self):
        self.assertEqual(max_integer([3]), 3)

    def test_string(self):
        self.assertEqual(max_integer(['m', 'a', 'x']), 'x')

    def test_ordered_num(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_num(self):
        self.assertEqual(max_integer([2, 4, 1, 3]), 4)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_neg_num(self):
        self.assertEqual(max_integer([-2, -4]), -2)

if __name__ == '__main__':
    unittest.main()
