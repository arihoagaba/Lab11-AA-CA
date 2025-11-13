# https://github.com/arihoagaba/Lab11-AA-CA
# Partner 1: Ariho Agaba
# Partner 2: Colton Allen


import unittest
from calculator import add, sub, div, log

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2,2), 4)
        self.assertEqual(add(-16, 12), -4)
        self.assertEqual(add(1, -1), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub (2, 2), 0)
        self.assertEqual(sub(-16, 12), -28)
        self.assertEqual(sub(1, -1), 2)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertRaises(ZeroDivisionError, div, 10, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(10, 1), 0)
        self.assertEqual(log(19, 1), 0)
        self.assertEqual(log(5, 25), 2)

    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(ValueError, log, 10, 0)


# Do not touch this
if __name__ == "__main__":
    unittest.main()