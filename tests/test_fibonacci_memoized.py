import unittest
from fibonacci_memoized import generate_fibonacci_sequence_memoized

class TestFibonacciMemoized(unittest.TestCase):
    def test_first_ten_terms(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        result = generate_fibonacci_sequence_memoized(10)
        self.assertEqual(result, expected)

    def test_negative_terms(self):
        # Test for negative number of terms, expecting an empty list
        result = generate_fibonacci_sequence_memoized(-5)
        self.assertEqual(result, [])

    def test_zero_terms(self):
        # Test for zero terms, expecting an empty list
        result = generate_fibonacci_sequence_memoized(0)
        self.assertEqual(result, [])

    def test_one_term(self):
        # Test for one term, expecting [0]
        expected = [0]
        result = generate_fibonacci_sequence_memoized(1)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()