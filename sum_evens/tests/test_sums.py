import unittest
from sum_utils.sums import sum_evens

class TestSum(unittest.TestCase):
    def test_sum_evens_basic(self):
        self.assertEqual(sum_evens(10), 30)
    def test_sum_evens_edge(self):
        self.assertEqual(sum_evens(1), 0)
    def test_negative(self):
        # self.assertEqual(sum_evens(-5), 0)
        with self.assertRaises(ValueError):
            sum_evens(-5)
    

if __name__ == '__main__':
    unittest.main()