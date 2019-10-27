import unittest

from main import HappyOrNot


class HappyTest(unittest.TestCase):
    def test_happy(self):
        with self.subTest("get correct happy number"):
            happy_numbers = [49, 97, 130, 10]
            for happy in happy_numbers:
                self.assertTrue(HappyOrNot(happy))

