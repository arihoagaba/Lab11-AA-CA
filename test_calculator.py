# https://github.com/arihoagaba/Lab11-AA-CA
# Partner 1: Ariho Agaba
# Partner 2: Colton Allen


import unittest
from calculator import *

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
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3),6)
        self.assertEqual(mul(2,4),8)
        self.assertEqual(mul(2,0),0)
    def test_divide(self): # 3 assertions
        self.assertEqual(div(12,3),4)
        self.assertEqual(div(15,3),5)
        self.assertEqual(div(12,1),12)
    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertRaises(ZeroDivisionError, div, 10, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(10, 1), 0)
        self.assertEqual(log(19, 1), 0)
        self.assertEqual(log(5, 25), 2)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        self.assertRaises(ValueError,log(-1, 10))
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
      self.assertEqual(hypotenuse(3,4),5)
      self.assertEqual(hypotenuse(5,12),13)
      self.assertEqual(hypotenuse(20,21),29)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        self.assertRaises(ValueError, square_root(-1))
    #     # Test basic function
        self.assertEqual(square_root(4),2)
        self.assertEqual(square_root(9),3)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()