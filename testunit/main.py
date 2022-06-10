import unittest

class TestExample(unittest.TestCase):

    def test_sum_numbers(self):
        num1 = 10
        num2 = 20

        result = num1 + num2
        # expect 30 as result
        # assert result == 30
        self.assertEqual(result, 30)
    
    def test_subs_numbers(self):
        self.assertEqual(20 -10, 10)

if __name__ == '__main__':
    unittest.main()
