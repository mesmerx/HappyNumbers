import unittest

from main import HappyOrNot, NoCache


class HappyTest(unittest.TestCase):
    def test_happy_numbers_without_memory_cache(self):
        happy_class = HappyOrNot(cache=False)
        with self.subTest("get true with correct happy numbers"):
            happy_numbers = [49, 97, 130, 10]
            for happy in happy_numbers:
                self.assertTrue(happy_class.happy_or_not(happy))

        with self.subTest("get false with incorrect happy numbers"):
            happy_numbers = [0, 2, 3, 4, 5, 6]
            for happy in happy_numbers:
                self.assertFalse(happy_class.happy_or_not(happy))

    def test_happy_numbers_with_memory_cache(self):
        happy_class = HappyOrNot(cache=True)
        with self.subTest("get true with correct happy numbers"):
            happy_numbers = [49, 49, 97, 130, 10]
            for happy in happy_numbers:
                self.assertTrue(happy_class.happy_or_not(happy))

        with self.subTest("get false with incorrect happy numbers"):
            happy_numbers = [0, 2, 2, 3, 4, 5, 6]
            for happy in happy_numbers:
                self.assertFalse(happy_class.happy_or_not(happy))

    def test_happy_numbers_with_file_cache(self):
        happy_class = HappyOrNot(cache=True, cache_file='number.dat')
        with self.subTest("get true with correct happy numbers"):
            happy_numbers = [49, 49, 97, 130, 10]
            for happy in happy_numbers:
                self.assertTrue(happy_class.happy_or_not(happy))

        with self.subTest("get false with incorrect happy numbers"):
            happy_numbers = [0, 2, 2, 3, 4, 5, 6]
            for happy in happy_numbers:
                self.assertFalse(happy_class.happy_or_not(happy))

        with self.subTest("get error when no cache is set"):
            with self.assertRaises(NoCache):
                happy_class = HappyOrNot(cache=False, cache_file='number.dat')
