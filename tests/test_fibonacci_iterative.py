import unittest
from fibonacci_recursive import generate_fibonacci_sequence

class TestFibonacciRecursive(unittest.TestCase):
    
    def test_first_ten_terms(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        result = generate_fibonacci_sequence(10)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()